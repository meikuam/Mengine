import copy


# ------------------------------------------------------------------------------------------------
# Основной контейнер данных ----------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
class MainContainer:
    '''
    Класс, который хранит чисто данные о наборе. Смысл контейнера - хранение наборов одинаковых однородных данных.
    Например: набор объектов графа, набор SERP объектов, наборов со статистикой директа, наборов запросов т.п. .
    В контейнере есть возможность использования индекса как "простых" типов: int, str, float; так и более сложных
    типа tuple. Ограничение связано с индексом в словарях python. Не рекомендуется float, лучше брать тогда tuple.

    max_key дефолтно меет значения: для int - 0, для  float - 0.0, для str - '', для tuple - (), иначе - None.
        Кроме того, "default" индекс в "добавлении элементов" может быть использован только для int и float,
        в противном случае - для str и tuple функция добавления выдаст ошибку, так как сдвиг max_index не возможен.

    В нём нет функции create, т.к. в произвольномслучае она не будет работать так же хорошо, как создание объекта
    вне контейнера и передачу его через add_object.
        Property (без setter):
            identification_object - получить идентифицирующий объект

            objects_dict - получить копию словаря с объектами

            dict_keys - получить ключи словаря с параметрами

            max_key - получить максимальное занятое значение целого ключа

            elements_amount - количество элементов в контейнере

        Менеджмент объектов:
            check_access - проверка объекта по индексу

            get_object - получить объект

            add_object - добавить готовый объект класса объектов контейнера

            del_object - удалить объект
        '''

    def __init__(self, objects_type: object,
                 identification_object: object = None,
                 index_type: int or float or str or tuple = int,
                 ):
        '''
        :param objects_type: тип объектов, которые будут находитсья в контейнере
        :param identification_object: "опознавательный объект". Это может быть id, строка, словарь, контейнер и прочее.
            А может ничего не быть.
        :param index_type: тип индексов, которые мы используем. Очевидно, презюмируется что все индексы имеют один и
            тот же тип. В противном случае можно использовать tuple, содержащий индекс внутри.
        '''

        self.__objects_type = objects_type  # Запомним тип объектов
        self.__index_type = index_type  # запомнили тип индексов
        self.__objects_dict = {}

        self.__identification_object = identification_object  # запомним идекнтификационный объект


        # Создадим "дефолный" максимальный индекс
        if isinstance(index_type, float):
            self.__max_key = float(0)
        elif isinstance(index_type, int):
            self.__max_key = 0
        elif isinstance(index_type, str):
            self.__max_key = ''
        elif isinstance(index_type, tuple):
            self.__max_key = ()
        else:
            self.__max_key = None


    # ------------------------------------------------------------------------------------------------
    # Закроем данные через property ------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    @property
    def identification_object(self):
        '''
        Функция отдаёт оригинал (не копию) объекта, который идентифицирует контейнер. Смысл в том, чтобы

        :return: идентификационный объект
        '''
        return self.__identification_object

    @property
    def objects_type(self):
        '''
        Отдаёт тип объектов, находящихся в контейнере.

        :return: тип объектов контейнера
        '''
        return self.__objects_type

    @property
    def index_type(self) -> object:
        '''
        Возвращает тип использующегося индекса.

        :return:
        '''
        return self.__index_type

    @property  # функция отдаёт неглубокую копию
    def objects_dict(self) -> dict:
        '''
        Функция отдаёт неглубокую копию словаря. Это нужно для того, чтобы защитить внутренний словарь от изменений,
        при этом всё-таки, предоставить словарь с объектами.

        :return: словарь объектов
        '''
        return copy.copy(self.__objects_dict)

    @property
    def objects_list(self) -> list:
        '''
        Функция подготавливает и отдаёт список объектов, находящихся в контейнере.

        :return: список объектов
        '''
        export_list = []
        for key in self.__objects_dict.keys():  # Пошли по ключам словаря
            export_list.append(self.__objects_dict[key])
        return export_list

    @property
    def dict_keys(self) -> list:
        '''
        Функция предоставляет список с ключами словаря.

        :return: список ключей
        '''
        return list(self.__objects_dict.keys())

    @property
    def max_key(self) -> object:
        '''
        Функция отдаёт максимальный ЗАНЯТЫЙ целый индекс элементов словаря.

        :return: "максимальный индекс". Для строки или tuple вернётся None, кроме случаев, когда
            self.__max_key был задан вне контейнера.
        '''
        return self.__max_key

    @max_key.setter
    def max_key(self, value: object):
        '''
        Запоминает "максимальный" ключ в наборе. Должны соблюстись 2 условия: тип value совпадает с типом ключей,
        объект с таким ключём есть в контейнере. Это не проверяется, чтобы исключить "неочевидные ошибки" в работе.

        :return:
        '''
        self.__max_key = value
        return

    @property
    def elements_amount(self) -> int:
        '''
        Получить количество элементов, находящихся в контейнере.

        :return: число
        '''
        return len(self.dict_keys)

    # ------------------------------------------------------------------------------------------------
    # Менеджмент данных ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    def check_access(self, index:  str or int or float or tuple) -> bool:
        '''
        Првоерка наличия объекта на индексе

        :param index: индекс/имя в наборе
        :return: статус
        '''
        try:
            a = self.__objects_dict[index]
            return True
        except KeyError:
            return False

    def get_object(self, index:  str or int or float or tuple,
                   no_value: object = None) -> object or None:
        '''
        Функция возвращает объект или None

        :param index: индекс/имя в наборе
        :param no_value: что вернуть если объекта нет?
        :return: объект или None, если объекта нет
        '''
        try:
            return self.__objects_dict[index]
        except KeyError:
            return no_value

    def add_object(self, data_object: object,
                   replace: bool = True,
                   index: str or int or float or tuple = 'default') -> bool or int or None:
        '''
        Функция принимает объект типа, указанного в __init__ (objects_type)

        :param data_object: объект, который надо поместить в контейнер. Тип объекта self.__objects_type
        :param replace: заменить если индекс занят?
        :param index: индекс словаря, на который будет добавлен объект. По умолчанию это __max_key + 1
        :return: Если индекс указан явно: был ли свободен индекс? True - свободен, False - был занят.
                 Если индекс поставлен 'default' - вернёт индекс
                 В случае ошибки - None
        '''
        if not isinstance(data_object, self.__objects_type):  # Если тип неверный
            return None

        # Установим индекс
        if index == 'default':  # Если ставим дефолтный

            if isinstance(self.__index_type, int):  # Если у нас целый ключ
                # чтобы self.__max_key был всё время актуален
                self.max_key += 1  # Сначала крутанём
                new_index = self.max_key  # потом возьмём

            elif isinstance(self.__index_type, float):  # Если у нас с точкой ключ
                # чтобы self.__max_key был всё время актуален
                new_index = self.max_key  # потом возьмём
                new_index = float(int(new_index) + 1)  # интнем до целой части и плюсанём 1, и сделаем float
                self.max_key = new_index  # Запомним новое значение
                new_index = self.__max_key  # потом возьмём
            else:
                return None  # Если индекс имеет тип "строка" или "tuple", и индекс не задан - ошибка.
        else:
            if isinstance(index, self.__index_type):  # Если индекс верного типа
                new_index = index  # берём его
            else:  # если тип индекса неверный
                return None  # Вернём ошибку

            if isinstance(self.__index_type, int) or isinstance(self.__index_type, float):  # Если ключ - числовой индекс
                if new_index > self.max_key:  # Если значение больше текущего максимального
                    self.max_key = new_index  # заменим текущее на новое

        try:  # Првоерим, занят ли индекс
            a = self.__objects_dict[new_index]
            free = False
        except KeyError:
            free = True

        # Добавим в селф
        if free or replace:  # Если индекс свободен или разрешена замена
            self.__objects_dict[new_index] = data_object

        if index == 'default':  # если индекс определялся внутри функции
            return new_index  # вернём индекс
        else:  # Если индекс был подан заранее
            return free  # ну - вернём результат

    def del_object(self, index: str or int or float or tuple) -> bool:
        '''
        Функция пытается удалить объект

        :param index: индекс элемента, который мы удалим
        :return: True - объект был и он удалён, False - объекта не было
        '''
        try:
            self.__objects_dict.pop(index)
            return True  # Если объект был и успешно удалён
        except KeyError:
            return False  # Если объекта не было
