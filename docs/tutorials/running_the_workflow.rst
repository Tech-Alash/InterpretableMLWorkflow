Запуск workflow
========================================

На этой странице описан стандартный порядок запуска для воспроизведения всего workflow.

Шаг 1: создать или отредактировать YAML-настройку
===============================================================================

Сначала сгенерируй конфигурацию по умолчанию:

.. code-block:: bash

   python setup_experiments.py

Если нужно, после этого вручную измени ``setup_files/main.yaml``.

Шаг 2: запустить основной скрипт экспериментов
=====================================================================

Выполни:

.. code-block:: bash

   python experiment.py

На высоком уровне :func:`experiment.main` делает следующее:

* загружает ``setup_files/main.yaml``;
* выставляет ``experiment_parameters["output_folder"]`` в ``results/test_case/``;
* подготавливает сырые данные;
* разворачивает сетку параметров в dataframe экспериментов;
* убирает фактические дубликаты;
* запускает recursive forecast experiments;
* запускает out-of-bag importance experiments.

Что записывает ``run_experiments``
==================================================

Для каждого hash эксперимента workflow пишет pickle-файлы в ``results/test_case/``.
Имена кодируют и тип задачи, и сам hash, например:

* ``results_forecast<hash>.pickle``
* ``results_out-of-bag<hash>.pickle``
* ``importance_forecast_shapley_priority_<hash>.pickle``
* ``importance_forecast_permutation_<hash>.pickle``
* ``importance_oob_shapley_priority_period_<date>_<hash>.pickle``

Во время выполнения код также может создавать временные placeholder-файлы, чтобы разные процессы не считали один и тот же эксперимент повторно.

Шаг 3: агрегировать качество прогнозов
========================================================

Когда сырые файлы экспериментов уже созданы, собери forecasting predictions в плоскую таблицу:

.. code-block:: bash

   python collect_performance.py

Скрипт создаёт:

* ``results/aggregated/pred_all_test_case_raw.csv``

Шаг 4: агрегировать feature-importance outputs
====================================================================

После этого собери интерпретационные артефакты:

.. code-block:: bash

   python collect_importance_forecast.py
   python collect_importance_out_of_bag.py

Эти скрипты создают CSV-файлы, которые потом используются на этапе анализа.

Шаг 5: запустить Shapley regression
=================================================

Выполни:

.. code-block:: bash

   python shapley_regression.py

Скрипт читает агрегированный файл с forecast-time Shapley values, выбирает семейство моделей, усредняет повторные оценки по датам
и затем вызывает :func:`helpers.utils_importance.shapley_regression`.

Шаг 6: запустить R-скрипты анализа
=================================================

Для части финальных аналитических результатов репозиторий использует R:

* ``error_analysis.R``
* ``shapley_analysis.R``

Эти скрипты читают агрегированные CSV-файлы, созданные Python-конвейером.

Краткий checklist запуска
============================================

Если нужен короткий порядок воспроизведения, используй такую последовательность:

.. code-block:: bash

   python setup_experiments.py
   python experiment.py
   python collect_performance.py
   python collect_importance_forecast.py
   python collect_importance_out_of_bag.py
   python shapley_regression.py

Следующий шаг
==============================

Потом открой :doc:`results_and_interpretation`, чтобы понять, какие файлы появляются на выходе и как они связаны с рисунками из статьи.
