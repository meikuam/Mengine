'''
Тут находятся "основные" объекты графа:
    NodeIdentification - идентификационный объект элемента графа

    NodeRelationsList, NodeRelationsSet, NodeRelationsString - набор объектов для хранения данных
        (отличаются скоростью работы и занимаемой памятью)

    narrow_down - функция сужения связей вершины графа (NodeRelations)

    EdgeIdentification - идентификационный элемент ребра

'''

import copy  # Для копирования

from Graphs.MainObjects.GraphConfiguration import GraphConfiguration

# ------------------------------------------------------------------------------------------------
# Вершины ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
class NodeIdentification:
    '''
    Объект, реализующий опознание элемента графа.
    Методы и свойства:
        graph_configuration - опознавательный ключ графа

        label - метка

        element_id - индекс элемента или ссылка на сопоставленный объект.
    '''

    def __init__(self, element_id: str or int or float or tuple,
                 graph_configuration: GraphConfiguration,
                 label: object = None):
        '''
        :param element_id: индекс элемента или ссылка на сопоставленный объект.
        :param graph_configuration:  идентификационный ключ графа.
        :param label: метка элемента. Например его тип.
        '''
        self.__graph_configuration = graph_configuration
        self.__label = label
        self.__element_id = element_id  # Мой индекс

    # ------------------------------------------------------------------------------------------------
    # Основные данные --------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    @property
    def element_id(self) -> str or int or float or tuple:
        '''
        Получение индекса или сопоставленного элемента объекта графа

        :return: целое число
        '''
        return self.__element_id

    @property
    def graph_configuration(self) -> GraphConfiguration or None:
        '''
        Получение идентификатора графа.

        :return: объект - идентификатор или None, если его нет.
        '''
        return self.__graph_configuration

    @property
    def label(self) -> object:
        '''
        Получение метки элемента графа

        :return: метка
        '''
        return self.__label


class NodeRelationsList:
    '''
    Объект, который будет хранить в себе данные о связях указанного типа вершины с другими вершинами.
    Вид хранения - "в списке". Подходит когда объём памяти важнее скорости.

    Основные методы и свойства:
        element_id - индекс элемента графа

        related_ids - список индексов связанных элементов

        _reset() - очистить связи

        add_relation() - добавить связь

        check_relation() - проверить свзяь

        del_relation() - удалить связь
    '''

    def __init__(self, element_id: str or int or float or tuple):
        '''

        :param element_id: индекс элемента
        '''
        self.__element_id = element_id  # Мой индекс
        self.__relations = []  # Создадим объект хранения связей

    def _reset(self):
        '''
        Сбрасывает содержимое набора связей

        :return:
        '''
        self.__relations.clear()
        return

    @property
    def element_id(self) -> str or int or float or tuple:
        '''
        Получение индекса или сопоставленного элемента объекта графа

        :return: целое число
        '''
        return self.__element_id

    @property
    def related_ids(self) -> list:
        '''
        Функция отдаёт все связанные индексы

        :return:
        '''
        return self.__relations.copy()

    # ------------------------------------------------------------------------------------------------
    # Работа со связями ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    def add_relation(self, element_id: str or int or float or tuple):
        '''
        Функция добавляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        if not element_id in self.__relations:
            self.__relations.append(element_id)
        return

    def check_relation(self, element_id: str or int or float or tuple) -> bool:
        '''
        Функция проверяет связь с элементом

        :param element_id: индекс элемента
        :return: статус: True - связь есть, False - связи нет.
        '''
        if element_id in self.__relations:
            return True
        else:
            return False

    def del_relation(self, element_id: str or int or float or tuple):
        '''
        Функция удаляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        try:
            self.__relations.pop(self.__relations.index(element_id))
        except ValueError or IndexError:
            pass

        return


class NodeRelationsSet:
    '''
    Объект, который будет хранить в себе данные о связях указанного типа вершины с другими вершинами.
    Вид хранения - "в упорядоченном наборе". Подходит, когда требуется скорость, но не критична память.

    Основные методы и свойства:
        element_id - индекс элемента графа

        related_ids - список индексов связанных элементов

        _reset() - очистить связи

        add_relation() - добавить связь

        check_relation() - проверить свзяь

        del_relation() - удалить связь
    '''

    def __init__(self, element_id: str or int or float or tuple):
        '''

        :param element_id: индекс элемента
        '''
        self.__element_id = element_id  # Мой индекс
        self.__relations = set()  # Создадим объект хранения связей

    def _reset(self):
        '''
        Сбрасывает содержимое набора связей

        :return:
        '''
        self.__relations.clear()  # сделали чистый набор
        return

    @property
    def element_id(self) -> str or int or float or tuple:
        '''
        Получение индекса или сопоставленного элемента объекта графа

        :return: целое число
        '''
        return self.__element_id

    @property
    def related_ids(self) -> list:
        '''
        Функция отдаёт все связанные индексы

        :return:
        '''
        return list(self.__relations)

    # ------------------------------------------------------------------------------------------------
    # Работа со связями ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    def add_relation(self, element_id: str or int or float or tuple):
        '''
        Функция добавляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        self.__relations.add(element_id)
        return

    def check_relation(self, element_id: str or int or float or tuple) -> bool:
        '''
        Функция проверяет связь с элементом

        :param element_id: индекс элемента
        :return: статус: True - связь есть, False - связи нет.
        '''
        if element_id in self.__relations:
            return True
        else:
            return False

    def del_relation(self, element_id: str or int or float or tuple):
        '''
        Функция удаляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        self.__relations.discard(element_id)
        return


class NodeRelationsString:
    '''
    Объект, который будет хранить в себе данные о связях указанного типа вершины с другими вершинами.
    Вид хранения - "в строке". Подходит когда требуется экономия памяти и индекс связей int, float, str.
        Не конфликтующий с хранением в строке.

    Основные методы и свойства:
        element_id - индекс элемента графа

        related_ids - список индексов связанных элементов

        _reset() - очистить связи

        add_relation() - добавить связь

        check_relation() - проверить свзяь

        del_relation() - удалить связь
    '''

    __sep = '%;'

    def __init__(self, element_id: str or int or float):
        '''

        :param element_id: индекс элемента
        '''
        self.__element_id = element_id  # Мой индекс
        self.__relations = copy.copy(self.__sep)  # Создадим объект хранения связей

    def _reset(self):
        '''
        Сбрасывает содержимое набора связей

        :return:
        '''
        self.__relations = copy.copy(self.__sep)  # сделали чистый набор
        return

    @property
    def element_id(self) -> str or int or float:
        '''
        Получение индекса или сопоставленного элемента объекта графа
        :return: целое число
        '''
        return self.__element_id

    @property
    def related_ids(self) -> list:
        '''
        Функция отдаёт все связанные индексы

        :return:
        '''
        ids_list = self.__relations.split(self.__sep)
        ids_list = ids_list[1:len(ids_list) - 1]  # Сбросим пограничные пустые

        export = []
        if type(self.element_id) is int:
            for j in range(0, len(ids_list)):
                try:
                    export.append(int(ids_list[j]))
                except BaseException:
                    pass

        elif type(self.element_id) is float:
            for j in range(0, len(ids_list)):
                for j in range(0, len(ids_list)):
                    try:
                        export.append(float(ids_list[j]))
                    except BaseException:
                        pass

        elif type(self.element_id) is str:
            export = ids_list

        return ids_list

    # ------------------------------------------------------------------------------------------------
    # Работа со связями ------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    def add_relation(self, element_id: str or int or float):
        '''
        Функция добавляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        if not f'{self.__sep}{element_id}{self.__sep}' in self.__relations:
            self.__relations += f'{element_id}{self.__sep}'
        return

    def check_relation(self, element_id: str or int or float) -> bool:
        '''
        Функция проверяет связь с элементом

        :param element_id: индекс элемента
        :return: статус: True - связь есть, False - связи нет.
        '''
        if f'{self.__sep}{element_id}{self.__sep}' in self.__relations:
            return True
        else:
            return False

    def del_relation(self, element_id: str or int or float):
        '''
        Функция удаляет связь с элементом

        :param element_id: индекс элемента
        :return: ничего
        '''
        self.__relations = self.__relations.replace(f'{self.__sep}{element_id}{self.__sep}', f'{self.__sep}')
        return


def narrow_down(node_relations: NodeRelationsList or NodeRelationsSet or NodeRelationsString,
                ids_list_or_set: list or set,
                keep: bool = True):
    '''
    Функция, делающая сужения связей по заданному набору индексов. Задача функции в том, чтобы исключить из связей все
    элементы, которых нет в графе, чтобы избежать ошибок при обработке.
    Функция работает непосредственно с контейнером, изменяя его.

    :param node_relations: контейнер со связями
    :param ids_list_or_set: список или сет индексов, которые будут оставлены/удалены
    :param keep: оставить или удалить id из ids_list_or_set? True - оставить, False - удалить
    :return: ничего
    '''
    # Делаем сет для скорости обращений
    if isinstance(ids_list_or_set, list):
        ids_list_or_set = set(ids_list_or_set)

    if keep:  # Если оставляем только указанные
        for related_id in node_relations.related_ids:  # Пошли по индексам
            if not related_id in ids_list_or_set:  # Если индекс не разрешён
                node_relations.del_relation(related_id)  # Сбрасываем связь
    else:  # Если скинуть указанные
        for related_id in node_relations.related_ids:  # Пошли по индексам
            if related_id in ids_list_or_set:  # Если индекс не разрешён
                node_relations.del_relation(related_id)  # Сбрасываем связь
    return


# ------------------------------------------------------------------------------------------------
# Рёбра ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
class EdgeIdentification:
    '''
    Объект, реализующий опознание элемента графа.
    Методы и свойства:
        graph_configuration - опознавательный ключ графа

        label - метка

        weight - метка

        edge_type - тип связи

        from_id - индекс элемента от которого идёт связь

        to_id - индекс элемента к которому идёт связь
    '''

    def __init__(self, from_id: str or int or float or tuple,
                 to_id: str or int or float or tuple,
                 label: object = None,
                 weight: int or float = None,
                 edge_type: object = None,
                 graph_configuration: GraphConfiguration = None):
        '''
        :param from_id: индекс элемента от которого идёт связь
        :param to_id: индекс элемента к которому идёт связь
        :param label: метка связи (не тип!).
        :param weight: "вес" элемента.
        :param edge_type: тип связи элемента.
        :param graph_configuration:  идентификационный ключ графа.
        '''
        self.__graph_configuration = graph_configuration

        self.__edge_type = edge_type
        self.__from_id = from_id
        self.__to_id = to_id

        self.__label = label
        self.__weight = weight

    # ------------------------------------------------------------------------------------------------
    # Основные данные --------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------
    @property
    def graph_configuration(self) -> GraphConfiguration or None:
        '''
        Получение идентификатора графа.

        :return: объект - идентификатор или None, если его нет.
        '''
        return self.__graph_configuration

    @property
    def edge_type(self) -> object:
        '''
        Получение типа связи

        :return: тип связи
        '''
        return self.__edge_type

    @property
    def from_id(self) -> str or int or float or tuple:
        '''
        Получение индекса элемента от которого идёт связь

        :return: целое число
        '''
        return self.__from_id

    @property
    def to_id(self) -> str or int or float or tuple:
        '''
        Получение индекса элемента к которому идёт связь

        :return: целое число
        '''
        return self.__to_id

    @property
    def label(self) -> object:
        '''
        Получение метки связи

        :return: метка
        '''
        return self.__label

    @property
    def weight(self) -> int or float:
        '''
        "Вес" связи

        :return:
        '''
        return self.__weight

