"""
Сводные таблицы :
    1)Фильмы - Просмотры
    2)Фильмы - Средняя оценка
    3)Режиссер - Средняя оценка фильмов
    4)Пользователи - Email - Наличие подписки
"""

import pandas as pd
import numpy as np

def films_views(database):
    """
        :param database: DataFrame, объединенная таблица данных:
        :return ser: Series, сводная таблица, отсортированная по Фильмы / Просмотры
    """

    ser = database['Название Фильма'].value_counts()

    return ser


def films_avg_ratings(database):
    """
        :param database: DataFrame, объединенная таблица данных:
        :return pivot: DataFrame, сводная таблица, отсортированная по Фильмы / Средняя оценка
    """
    pivot = pd.pivot_table(database, values='Оценка', index='Название Фильма')

    return pivot


def director_avg_ratings(database):
    """
        :param database: DataFrame, объединенная таблица данных:
        :return pivot: DataFrame, сводная таблица, отсортированная по Режиссер / Средняя оценка фильмов
    """
    pivot = pd.pivot_table(database, values='Оценка', index='Режиссер')

    return pivot


def unpivot(frame):
    N, K = frame.shape
    data = {
        "value": frame.to_numpy().ravel("F"),
        "variable": np.asarray(frame.columns).repeat(N),
        "date": np.tile(np.asarray(frame.index), K),
    }
    return pd.DataFrame(data, columns=["date", "variable", "value"])


def users_email_subs(database):
    """
        :param database: DataFrame, объединенная таблица данных:
        :return user_info: DataFrame, сводная таблица, отсортированная по Пользователи / Email / Наличие подписки
    """
    user_info = pd.DataFrame(database, database.index, ['Имя пользователя', 'E-mail пользователя', 'Наличие Подписки'])
    # user_info = pd.crosstab(database, database.index, ['Имя пользователя', 'E-mail пользователя', 'Наличие подписки'])
    user_info = user_info.drop_duplicates(keep='first',
                                          subset=['Имя пользователя', 'E-mail пользователя', 'Наличие Подписки'])

    # print(database.index)
    return user_info



