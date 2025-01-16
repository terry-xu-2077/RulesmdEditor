from myTools import myJson
from ra2RulesParser import rulesParser

typesDict = {
    'InfantryTypes': '步兵类',
    'VehicleTypes': '战车类',
    'AircraftTypes': '飞机类',
    'BuildingTypes': '建筑类',
    'SuperWeaponTypes': '超武类',
    'Weapons': '武器类',
    'Warheads': '弹头类',
    'Projectiles': '弹体类'
}

typesID_Dict = {
    '步兵类': 'InfantryTypes',
    '战车类': 'VehicleTypes',
    '飞机类': 'AircraftTypes',
    '建筑类': 'BuildingTypes',
    '超武类': 'SuperWeaponTypes',
    '武器类': 'Weapons',
    '弹头类': 'Warheads',
    '弹体类': 'Projectiles'
}

userDescINI = rulesParser('Resources/UserDesc.ini')
modDescINI = rulesParser('Resources/ModDesc.ini')


def unit_get_owner(rules, key):
    unit_sides = []
    pre_list = rules[key].get('Prerequisite').split(',')
    for pre_unit in pre_list:
        if pre_unit.upper() not in ['TECH', 'BARRACKS', 'POWER', 'PROC', 'RADAR']:
            if rules[pre_unit] is None:
                continue
            if not rules[pre_unit].get('Prerequisite') is None:
                unit_sides = unit_get_owner(rules, pre_unit)
            elif not rules[pre_unit].get('Owner') is None:
                unit_sides = rules[pre_unit].get('Owner').split(',')
    return unit_sides


def is_in_sides(sides, rules, key, air=False) -> bool:
    unit_sides = []
    if air:
        if not rules[key].get('Owner') is None:
            unit_sides = rules[key].get('Owner').split(',')

    elif not rules[key].get('Prerequisite') is None:
        unit_sides = unit_get_owner(rules, key)

    elif rules[key].get('UndeploysInto'):
        if not rules[key].get('Owner') is None:
            unit_sides = rules[key].get('Owner').split(',')

    if len(unit_sides) > len(sides):
        return False
    if [True for x in unit_sides if x in sides]:
        return True
    else:
        return False


class IdentifyTypeINI:
    INI = rulesParser('Resources/IdentType.ini', )

    @classmethod
    def get_ident_list(cls, type_name, option):
        value = cls.INI.get(type_name, option)
        if value:
            return value.strip().replace('，', ',').split(',')
        else:
            return []


class ident_class:
    must = []
    multi = []
    exclude = []


class handle_sections:
    root_sections = ('InfantryTypes', 'VehicleTypes', 'AircraftTypes', 'BuildingTypes', 'SuperWeaponTypes',
                     'Weapons', 'Warheads', 'Projectiles')
    weapon_options = ('Primary', 'Secondary', 'OccupyWeapon', 'EliteOccupyWeapon', 'ElitePrimary',
                      'EliteSecondary', 'DeathWeapon', 'Weapon1', 'EliteWeapon1', 'Weapon2', 'EliteWeapon2',
                      'Weapon3', 'EliteWeapon3', 'Weapon4', 'EliteWeapon4', 'Weapon5', 'EliteWeapon5',
                      'Weapon6', 'EliteWeapon6', 'ShrapnelWeapon')

    ident_dict = {
        'Weapons': ident_class(),
        'Warheads': ident_class(),
        'Projectiles': ident_class(),
    }

    ident_dict['Weapons'].must = IdentifyTypeINI.get_ident_list('Weapons', 'must')
    ident_dict['Weapons'].multi = IdentifyTypeINI.get_ident_list('Weapons', 'multi')
    ident_dict['Weapons'].exclude = IdentifyTypeINI.get_ident_list('Weapons', 'exclude')

    ident_dict['Warheads'].must = IdentifyTypeINI.get_ident_list('Warheads', 'must')
    ident_dict['Warheads'].multi = IdentifyTypeINI.get_ident_list('Warheads', 'multi')
    ident_dict['Warheads'].exclude = IdentifyTypeINI.get_ident_list('Warheads', 'exclude')

    ident_dict['Projectiles'].must = IdentifyTypeINI.get_ident_list('Projectiles', 'must')
    ident_dict['Projectiles'].multi = IdentifyTypeINI.get_ident_list('Projectiles', 'multi')
    ident_dict['Projectiles'].exclude = IdentifyTypeINI.get_ident_list('Projectiles', 'exclude')


class helpINI:
    helpINI = rulesParser('Resources/HelpInfor.ini', )

    def get_help_info(self, option):
        if self.helpINI.has_option('HelpInfo', option):
            text = self.helpINI.get('HelpInfo', option).replace('\\n', '\n')
            try:
                if self.helpINI.has_section(option + '_List'):
                    text += '\n\n'
                    for key in self.helpINI.options(option + '_List'):
                        text += key + '=' + self.helpINI.get(option + '_List', key).strip().replace('\\n', '\n') + '\n'
                    return text
            except Exception as e:
                print(e)
            return text
        return ''


class optionINI:
    optionsDescINI = rulesParser('Resources/OptionsDesc.ini', )

    Country_options = optionsDescINI.get('MultipleMenu', 'Country_Type')
    Abilities_options = optionsDescINI.get('MultipleMenu', 'Abilities_Type')
    Buildings_options = optionsDescINI.get('MultipleMenu', 'Buildings_Type')

    def get_option_menu(self, option):
        option = option + '_List'
        if self.optionsDescINI.has_section(option):
            return self.optionsDescINI.items(option)
        return []

    def get_option_menu_value(self, option, index):
        option = option + '_List'
        keys = self.optionsDescINI.options(option)
        return keys[index]

    def get_option_desc(self, option):
        if self.optionsDescINI.has_option('OptionDesc', option):
            return self.optionsDescINI.get('OptionDesc', option)
        return ''


class namesINI:
    namesINI = rulesParser('Resources/NamesDesc.ini', )

    def get_type_sectionDesc(self, root):
        return self.namesINI.get('TypeDesc', root)

    def get_UIName_desc(self, option):
        if self.namesINI.has_option('NameDesc', option):
            return self.namesINI.get('NameDesc', option)
        return ''


class myIniClass(handle_sections, optionINI, helpINI, namesINI):
    def __init__(self, callback):
        self.rulesmdINI = rulesParser(readDesc=True)
        self.newOptions = {}
        self.callback = callback
        self.rulesType = ''
        # 数据库
        self.building_list = []
        self.image_dict = {}
        self.weapon_dict = {}
        self.warhead_dict = {}
        self.projectile_dict = {}
        self.sound_dict = {}
        self.add_options_dict = {}
        self.add_section_dict = {}
        self.side_dict = {}
        self.quote_dict = {}

    def open_rules_file(self, rules_file):
        self.rulesmdINI.read_file(rules_file)
        if 'Mental Omega' in self.rulesmdINI['General']['Name']:
            self.rulesType = 'MentalOmega'
        else:
            self.rulesType = ''

    def get_Name(self, section):
        if self.rulesmdINI.has_option(section, 'Name'):
            return self.rulesmdINI.get(section, 'Name')
        return ''

    def get_rules_section_ID(self, section):
        try:
            for key in self.root_sections:
                for item in self.rulesmdINI.items(key):
                    if item[1] == section:
                        return [key, item[0]]
        except:
            return None

    def get_rules_section_newID(self, itemType):
        id_list = []
        if self.rulesmdINI.has_section(itemType):
            for x in self.rulesmdINI.items(itemType):
                id_list.append(int(x[0]))
            id_list.sort()
            return str(id_list[-1] + 1)
        else:
            return None

    def clear_rules_section(self, section):
        if self.rulesmdINI.has_section(section):
            for i in self.rulesmdINI.items(section):
                self.rulesmdINI.remove_option(section, i[0])

    def save_rules_section_backup(self, section, file):
        if self.rulesmdINI.has_section(section):
            newINI = rulesParser()
            data = self.rulesmdINI.items(section)
            sec_id = self.get_rules_section_ID(section)
            if sec_id != None:
                newINI.add_section(sec_id[0])
                newINI.set(sec_id[0], section, sec_id[1])
            if data:
                newINI.add_section(section)
                for i in data:
                    newINI.set(section, *i)
            newINI.write_file(file)
        else:
            self.callback(ini_error='此项目不存在于ini中:' + section)
            return False

    def replace_from_file(self, section, file):
        newINI = rulesParser(file)

        if len(newINI.sections()) != 2:
            self.callback(ini_error='此备份结构暂不支持')
            return False

        back_section = section
        if not newINI.has_section(section):
            keys = newINI.sections()
            if len(keys) == 2:
                back_section = keys[1]
                rep = self.callback(sure='此备份非此单位的备份, 请选择你的操作', button=[(0, '替换'), (-1, '取消')])
                if rep == -1:
                    return False

        if not newINI.items(back_section):
            self.callback(ini_error='无效的ini文件')
            return False

        sec_tyoe = ''
        sec_id = ''
        for key in self.root_sections:
            if newINI.has_section(key):
                sec_tyoe = key
                sec_id = newINI.get(key, back_section)
                break

        if not sec_id:
            self.callback(ini_error='此备份有错误，无单位注册码')
            return False

        if self.rulesmdINI.get(sec_tyoe, sec_id) != section:
            rep = self.callback(sure='此备份中的单位注册码与rules中的不一致，请选择你的操作',
                                button=[(0, '忽略备份中的'), (2, '使用备份中的替换'), (1, '新建注册码'), (-1, '取消')])
            if rep == 2:  # 替换
                self.rulesmdINI.set(sec_tyoe, sec_id, section)
            elif rep == 1:  # 新建
                new_sec_id = self.get_rules_section_newID(sec_tyoe)
                self.rulesmdINI.set(sec_tyoe, new_sec_id, section)
            elif rep == -1:
                return False

        self.clear_rules_section(section)
        for i in newINI.items(back_section):
            self.rulesmdINI.set(section, *i)
        return True

    def get_rules_other_unit(self, type_name):
        unit_list = []
        for key in self.rulesmdINI.sections():
            has_option = True
            added = False
            jump = False

            if self.ident_dict[type_name].exclude:  # 只要存在其中一个就行
                for exclude in self.ident_dict[type_name].exclude:
                    if self.rulesmdINI.has_option(key, exclude):
                        jump = True
                        break
                if jump:  # 如果存在则跳过此section
                    continue

            if self.ident_dict[type_name].must:  # 必须存在的
                for must in self.ident_dict[type_name].must:
                    has_option = self.rulesmdINI.has_option(key, must)
                if not has_option:  # 如果不存在则跳过此section
                    continue

            if self.ident_dict[type_name].multi:  # 只要存在其中一个就行
                for multi in self.ident_dict[type_name].multi:
                    if self.rulesmdINI.has_option(key, multi):
                        unit_list.append(key)
                        added = True
                if not added:  # 如果未添加则跳过此section
                    continue

            if not added:  # 如果到了这里还没添加，则添加
                if has_option:
                    unit_list.append(key)

        return unit_list

    def get_rules_TypeListSections(self):
        root_dict = {}
        for key in self.root_sections:
            if key == 'Weapons':
                root_dict.setdefault(key, self.get_rules_other_unit(key))
            elif key == 'Warheads':
                root_dict.setdefault(key, self.get_rules_other_unit(key))
            elif key == 'Projectiles':
                root_dict.setdefault(key, self.get_rules_other_unit(key))
            else:
                items = []
                if self.rulesmdINI.has_section(key):
                    for option, value in self.rulesmdINI.items(key):
                        section = value
                        if self.rulesmdINI.has_section(section):
                            items.append([section, option])
                root_dict.setdefault(key, items)
        return root_dict

    def get_rules_jumpLink_list(self, value, get_item=True):
        keys = self.rulesmdINI.sections()
        link_list = []
        for key in keys:
            if key not in self.root_sections:
                if self.rulesmdINI.has_section(key):
                    for item in self.rulesmdINI.items(key):
                        if item[1] == value:
                            if get_item:
                                link_list.append([key, *item])
                            else:
                                link_list.append(key)
                            break
        return link_list

    def get_rules_LinkNameDesc(self, value):
        link_1 = self.get_rules_jumpLink_list(value, False)  # 武器
        unitDesc_list = []
        for wep in link_1:
            link = self.get_rules_jumpLink_list(wep, False)  # 单位
            for unit in link:
                name = self.get_UIName_desc(unit)
                if not name:
                    name = unit
                unitDesc_list.append(name)
        return unitDesc_list

    def get_voiceSound_dict(self):
        result = myJson(data={
            '步兵': {},
            '战车': {},
            '飞机': {},
            '建筑': {},
        })
        for key in self.rulesmdINI.sections():
            parent = None
            if self.rulesmdINI.has_option(key, 'Category'):
                type_name = self.rulesmdINI.get(key, 'Category')
                if type_name in ['Transport', 'Support', 'LRFS', 'IFV', 'AFV']:
                    parent = '战车'
                elif type_name in ['AirLift', 'AirPower']:
                    parent = '飞机'
                elif type_name in ['Soldier', 'Civilian']:
                    parent = '步兵'
            elif self.rulesmdINI.has_option(key, 'BuildCat'):
                parent = '建筑'

            if parent != None:
                value_dict = {}

                name = self.rulesmd_get_UIName_desc(key)
                if not name:
                    name = key

                for option, value in self.rulesmdINI.items(key):
                    if 'Voice' in option or 'Sound' in option:
                        try:
                            optionDesc = self.optionsDescINI.get('OptionDesc', option)
                        except:
                            optionDesc = option

                        if not optionDesc:
                            optionDesc = option

                        value_dict.setdefault('{0} . {1}'.format(name, optionDesc), value)
                if value_dict:
                    result[parent].setdefault(name, value_dict)
        return result

    def get_weapons_dict(self):
        result = myJson(data={
            '步兵类': {},
            '战车类': {},
            '飞机类': {},
            '建筑类': {},
            '弹体类': {},
            '未分类': {}
        })
        weapon_list = self.get_rules_other_unit('Weapons')
        for x in typesDict.keys():
            if self.rulesmdINI.has_section(x):
                for i, key in self.rulesmdINI.items(x):
                    if self.rulesmdINI.has_section(key):
                        section_weapons = {}
                        name = self.rulesmd_get_UIName_desc(key)
                        if not name:
                            name = key
                        for option, value in self.rulesmdINI.items(key):
                            if option in self.weapon_options:
                                for v, w in enumerate(weapon_list):
                                    if value == w:
                                        valueDesc = self.rulesmd_get_UIName_desc(value)
                                        if not valueDesc:
                                            valueDesc = value
                                        optionDesc = self.optionsDescINI.get('OptionDesc', option)
                                        if not optionDesc:
                                            optionDesc = option
                                        section_weapons.setdefault(
                                            '{0} . {1} . {2}'.format(name, optionDesc, valueDesc), weapon_list.pop(v))
                        if section_weapons:
                            if result.get(typesDict[x]) is None:
                                continue
                            result[typesDict[x]].setdefault(name, section_weapons)
        if weapon_list:
            for i, w in enumerate(weapon_list):
                valueDesc = self.rulesmd_get_UIName_desc(w)
                if not valueDesc:
                    valueDesc = 'NONE: ' + w
                result['未分类'].setdefault(valueDesc, {valueDesc + ' . ' + w: w})
        return result

    def get_warheads_dict(self):
        result = myJson(data={
            '弹头类': {},
        })
        warhead_list = self.get_rules_other_unit('Warheads')
        for key in warhead_list:

            name = self.rulesmd_get_UIName_desc(key)  # 如果没有上级则设置value为选项
            if not name:
                name = key
            result['弹头类'].setdefault(name, {key: key})
        return result

    def get_projectile_dict(self):
        result = myJson(data={
            '弹体类': {},
        })
        warhead_list = self.get_rules_other_unit('Projectiles')
        for key in warhead_list:

            name = self.rulesmd_get_UIName_desc(key)  # 如果没有上级则设置value为选项
            if not name:
                name = key
            result['弹体类'].setdefault(name, {key: key})
        return result

    def get_options_dict(self):
        def get_options(section):
            for item in self.rulesmdINI.items(section):
                option = item[0]
                value = item[1]
                try:
                    name = self.optionsDescINI.get('OptionDesc', option)
                except:
                    name = option
                def_value = value
                if result[typesDict[x]].get(name) is None:
                    result[typesDict[x]].setdefault(name, {option: def_value})

        result = myJson(data={
            '步兵类': {},
            '战车类': {},
            '飞机类': {},
            '建筑类': {},
            '超武类': {},
            '武器类': {},
            '弹头类': {},
            '弹体类': {},
        })
        for x in typesDict.keys():
            if self.rulesmdINI.has_section(x):
                for i in self.rulesmdINI.items(x):
                    if self.rulesmdINI.has_section(i[1]):
                        get_options(i[1])
            elif x == 'Weapons':
                for section in self.get_rules_other_unit(x):
                    get_options(section)
            elif x == 'Warheads':
                for section in self.get_rules_other_unit(x):
                    get_options(section)
            elif x == 'Projectiles':
                for section in self.get_rules_other_unit(x):
                    get_options(section)

        return result

    def get_unitName_dict(self, image=False):
        result = myJson(data={
            '步兵类': {},
            '战车类': {},
            '飞机类': {},
            '建筑类': {}
        })
        for key in self.rulesmdINI.sections():
            if self.rulesmdINI.has_option(key, 'Category') or self.rulesmdINI.has_option(key, 'BuildCat'):
                try:
                    type_name = self.rulesmdINI.get(key, 'Category')
                except:
                    type_name = 'BuildCat'

                name = key
                value = key

                if image:
                    if self.rulesmdINI.has_option(key, 'Image'):
                        value = self.rulesmdINI.get(key, 'Image')

                if self.rulesmdINI.has_option(key, 'NameDesc'):
                    name = self.rulesmdINI.get(key, 'NameDesc').split(':', 1)[1]

                nameDesc = self.rulesmd_get_UIName_desc(key)
                if not nameDesc:
                    nameDesc = self.rulesmd_get_UIName_desc(key.upper())

                if nameDesc:
                    name = nameDesc
                else:
                    name = key

                if type_name in ['Transport', 'Support', 'LRFS', 'IFV', 'AFV']:
                    result['战车类'].setdefault(name, value)
                elif type_name in ['AirLift', 'AirPower']:
                    result['飞机类'].setdefault(name, value)
                elif type_name in ['Soldier', 'Civilian']:
                    result['步兵类'].setdefault(name, value)
                elif type_name == 'BuildCat':
                    result['建筑类'].setdefault(name, value)

        return result

    def get_building_list(self):
        building_list = []
        for i, key in self.rulesmdINI.items('BuildingTypes'):
            if self.rulesmdINI.has_section(key):
                if self.rulesType:
                    desc = modDescINI.get(self.rulesType + '_Buildings', key)
                else:
                    desc = self.rulesmd_get_UIName_desc(key)
                if not desc:
                    desc = key

                # 可造建筑
                if self.rulesmdINI.has_option(key, 'TechLevel'):
                    value = self.rulesmdINI.get(key, 'TechLevel')
                    if value != '-1':
                        building_list.append((key, desc))
                        continue

                # 为建造场
                if self.rulesmdINI.has_option(key, 'UndeploysInto'):
                    building_list.append((key, desc))

        return building_list

    def get_quote_section(self, section):
        quote_dict = {}
        for key in self.rulesmdINI.sections():
            if key not in ['OverlayTypes', 'General', 'InfantryTypes', 'VehicleTypes', 'AircraftTypes',
                           'BuildingTypes']:
                if self.rulesmdINI.has_section(key):
                    for option, value in self.rulesmdINI.items(key):
                        if option not in ['Image']:
                            if value == section:
                                desc = self.get_UIName_desc(key)
                                if not desc:
                                    desc = key
                                quote_dict.setdefault(desc, key)
        return quote_dict

    def get_section_dict(self):
        def get_sectionDesc_dict(section):
            sectionDesc = self.rulesmd_get_UIName_desc(section)
            if not sectionDesc:
                # link_names = []
                # for n in self.get_rules_jumpLink_list(section, False):
                #     link_names.append(self.get_UIName_desc(n))
                # sectionDesc = section + '   [{0}]'.format(','.join(link_names))
                sectionDesc = section
            return [sectionDesc, section]

        root_dict = {}
        for key in self.root_sections:

            keyDesc = self.namesINI.get('TypeDesc', key)
            if not keyDesc:
                keyDesc = key

            # todo 加入弹头列表
            if key == 'Warheads':
                items = {}
                list_1 = self.get_rules_other_unit(key)
                list_2 = []
                for i, section in self.rulesmdINI.items(key):
                    list_2.append(section)
                warheads = list(set(list_1 + list_2))
                for section in warheads:
                    if self.rulesmdINI.has_section(section):
                        items.setdefault(*get_sectionDesc_dict(section))
                root_dict.setdefault(keyDesc, items)

            elif key == 'Weapons':
                items = {}
                weapons = self.get_rules_other_unit(key)
                for section in weapons:
                    if self.rulesmdINI.has_section(section):
                        items.setdefault(*get_sectionDesc_dict(section))
                root_dict.setdefault(keyDesc, items)

            elif key == 'Projectiles':
                items = {}
                projectiles = self.get_rules_other_unit(key)
                for section in projectiles:
                    if self.rulesmdINI.has_section(section):
                        items.setdefault(*get_sectionDesc_dict(section))
                root_dict.setdefault(keyDesc, items)

            else:
                items = {}
                for i, section in self.rulesmdINI.items(key):
                    if self.rulesmdINI.has_section(section):
                        items.setdefault(*get_sectionDesc_dict(section))
                root_dict.setdefault(keyDesc, items)
        return root_dict

    def rulesmd_add_unit(self, item):
        type_name, type_id, section_name, nameDesc, items = item

        if type_id:  # 注册
            self.rulesmdINI.set(type_name, type_id, section_name)

        self.rulesmdINI.add_section(section_name)  # 创建对象

        if type_name in ['InfantryTypes', 'VehicleTypes', 'AircraftTypes', 'BuildingTypes']:
            image = ''
            for i in items:
                if i[0] == 'UIName':
                    image = i[1].split(':', 1)[1]
                    break
            if image:
                option_list = [i[0] for i in items]
                if 'Image' not in option_list:
                    items.insert(1, ['Image', image])

        for option, value in items:
            if option == 'UIName':
                value = 'Name:' + section_name
            if option == 'Name':
                value = nameDesc
            self.rulesmdINI.set(section_name, option, value)

        if nameDesc:
            self.namesINI.set('NameDesc', section_name, nameDesc)

        if type_name == 'Weapons':
            if not self.rulesmdINI.has_option(section_name, 'Warhead'):
                self.rulesmdINI.set(section_name, 'Warhead', 'none')

        elif type_name == 'Projectiles':
            if not self.rulesmdINI.has_option(section_name, 'Inviso'):
                self.rulesmdINI.set(section_name, 'Inviso', 'no')

    def rulesmd_get_side_dict(self):
        type_list = ['BuildingTypes', 'InfantryTypes', 'VehicleTypes', 'AircraftTypes']
        side_dict = {
            '全部': {
                'BuildingTypes': [],
                'InfantryTypes': [],
                'VehicleTypes': [],
                'AircraftTypes': [],
                'SuperWeaponTypes': [],
                'WeaponTypes': [],
                'name': 'all',
                'list': []
            }
        }
        for i in self.rulesmdINI.items('Sides'):
            if i[0] in ['Civilian', 'Mutant']:
                continue
            if self.rulesType:
                desc = modDescINI.get(self.rulesType + '_Sides', i[0])
            else:
                desc = self.namesINI['SideDesc'].get(i[0])
                if not desc:
                    desc = self.namesINI['SideDesc'].get(i[1])

            if not desc:
                desc = i[1]
            side_dict.setdefault(desc, {
                'BuildingTypes': [],
                'InfantryTypes': [],
                'VehicleTypes': [],
                'AircraftTypes': [],
                'SuperWeaponTypes': [],
                'WeaponTypes':[],
                'name': i[0],
                'list': i[1].strip().split(',')
            })
        # 获取单位
        air = False
        for type_name in type_list:
            for uid, unit in self.rulesmdINI.items(type_name):
                if self.rulesmdINI[unit] is None:
                    continue
                for side in side_dict.keys():
                    if type_name == 'AircraftTypes':
                        air = True
                    if side != '全部':
                        if is_in_sides(side_dict[side]['list'], self.rulesmdINI, unit, air):
                            side_dict[side][type_name].append(unit)

        for side in side_dict.keys():
            for unit in side_dict[side]['BuildingTypes']:
                superWeapon = self.rulesmdINI.get(unit, 'SuperWeapon')
                if superWeapon:
                    side_dict[side]['SuperWeaponTypes'].append(superWeapon)
                    continue

        # for side in side_dict.keys():
        #     for type_name in type_list:
        #         for unit in side_dict[side][type_name]:
        #             for wp in self.weapon_options:
        #                 weapon = self.rulesmdINI.get(unit, wp)
        #                 if weapon:
        #                     side_dict[side]['WeaponTypes'].append(weapon)


        return side_dict

    def rulesmd_get_option_desc(self, section, option):
        desc = userDescINI.get('OptionDesc', option)
        if desc:
            return desc

        desc = self.get_option_desc(option)
        if desc:
            return desc

        desc = self.rulesmdINI.get_option_desc(section, option)
        if desc:
            return desc

        return ''

    def rulesmd_get_UIName_desc(self, section):
        desc = userDescINI.get('NameDesc', section)
        if desc:
            return desc

        if self.rulesType:
            for x in ['_Units', '_Buildings']:
                desc = modDescINI.get(self.rulesType + x, section)
                if desc:
                    return desc

        desc = self.get_UIName_desc(section)
        if desc:
            return desc

        desc = self.rulesmdINI.get_section_desc(section)
        if desc:
            return desc

        return ''

    def rulesmd_get_option_menu(self, option):
        menu_list = []
        if option == 'Country':
            countries = self.rulesmdINI.items('Countries')
            for i in countries:
                if i[1] in ['Neutral', 'Special']:
                    continue
                if self.rulesType:
                    desc = modDescINI.get(self.rulesType + '_Countries', i[1])
                else:
                    desc = self.optionsDescINI['Country_List'].get(i[1])
                if desc is None:
                    desc = i[1]
                menu_list.append([i[1], desc])
        elif option == 'Armor':
            if self.rulesType:
                menu_list = modDescINI.items(self.rulesType + '_Armor')
            else:
                menu_list = self.get_option_menu(option)
        elif option == 'Buildings':
            menu_list = self.get_option_menu(option)
            if self.building_list:
                menu_list.extend(self.building_list)
        else:
            menu_list = self.get_option_menu(option)
        return menu_list

    @staticmethod
    def save_desc_INI():
        userDescINI.write_file()

    def set_user_option_desc(self, option, value):
        userDescINI.set('OptionDesc', option, value)

    def set_user_Name_desc(self, option, value):
        userDescINI.set('NameDesc', option, value)


if __name__ == '__main__':
    def callback(info):
        print(info)


    ini = myIniClass(callback)
    f1 = 'XXX/rulesmo_心灵终结3.5.5.ini'
    f2 = 'Resources/rulesmd.pre'
    f3 = 'XXX/rulesmd-x.ini'
    ini.open_rules_file(f1)
    side_dict = ini.rulesmd_get_side_dict()
    for k in side_dict.keys():
        print(k, side_dict[k])
