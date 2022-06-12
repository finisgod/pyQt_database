import sys
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# PLOTS
from DB import films_views


class PlotFilmRatingCanvas(FigureCanvas):
    def __init__(self, parent, db):
        fig, self.ax = plt.subplots(figsize=(2, 2), dpi=60)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        data = pd.pivot_table(db, values='Оценка', index='Название Фильма').to_dict()
        data = data['Оценка']
        data_keys = list(data.keys())
        y_pos = np.arange(len(data_keys))
        data_values = list(data.values())

        fig1, ax = plt.subplots()
        hbars = self.ax.barh(y_pos, data_values, align='center')
        self.ax.invert_yaxis()
        self.ax.set_xlabel('Оценка')
        self.ax.set_ylabel('Место')
        self.ax.set_title('Рейтинг фильмов')
        self.ax.bar_label(hbars, fmt='%.2f')
        self.ax.bar_label(hbars, labels=data_keys, label_type='center')
        self.ax.set_xlim(right=10)

        self.ax.grid()


class PlotFilmRatingScatterCanvas(FigureCanvas):
    def __init__(self, parent, db):
        fig, self.ax = plt.subplots(figsize=(2, 2), dpi=60)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        # plt.style.use('_mpl-gallery')

        # make the data
        data = pd.pivot_table(db, values='Оценка', index='Название Фильма').to_dict()
        data = data['Оценка']
        data_keys = list(data.keys())
        y_pos = np.arange(len(data_keys))
        data_values = list(data.values())
        # size and color:
        # sizes = np.random.uniform(15, 80, len(x))
        # colors = np.random.uniform(15, 80, len(x))

        # plot
        fig, ax = plt.subplots()

        self.ax.scatter(data_values, data_keys)

        self.ax.set_title('Рейтинг фильмов')
        # ax.bar_label(hbars, fmt='%.2f')
        self.ax.set_xlim(right=10)

        self.ax.grid()


class PlotFilmViewsCanvas(FigureCanvas):
    def __init__(self, parent, db):
        fig, self.ax = plt.subplots(figsize=(2, 2), dpi=60)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        ser = db['Название Фильма'].value_counts()
        data_values = ser.array
        data_keys = list(ser.to_dict().keys())
        y_pos = np.arange(1, len(data_values) + 1)

        fig, ax = plt.subplots()
        hbars = self.ax.barh(y_pos, data_values, align='center')
        self.ax.set_title('Фильмы по просмотрам')
        self.ax.set_xlabel('Количество просмотров')
        self.ax.set_ylabel('Место')
        self.ax.bar_label(hbars, labels=data_keys, label_type='center')


class PlotAvgMarksCanvas(FigureCanvas):
    def __init__(self, parent, db):
        fig, self.ax = plt.subplots(figsize=(2, 2), dpi=60)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        fig1, ax = plt.subplots()
        self.ax.hist(films_views(db))
        self.ax.set_title('Оценки по частоте')
        self.ax.set_ylabel('Количество фильмов')
        self.ax.set_xlabel('Количество просмотров')

        self.ax.grid()

class PlotBoxCanvas(FigureCanvas):
    def __init__(self, parent, db):
        fig, self.ax = plt.subplots(figsize=(2, 2), dpi=60)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        ser = films_views(db)

        fig1, ax = plt.subplots()
        self.ax.set_title('Диаграмма Бокса-Вискера для среднего количеста просмотров')
        self.ax.set_ylabel('Количество просмотров')
        self.ax.boxplot(ser)


