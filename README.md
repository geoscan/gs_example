# Описание пакета gs_example

## Описание:
В данном пакете находятся базовые примеры

## Состав пакета:
1. Ноды:
    * board_test.py - пример получения бортовой информации
    * flight_test.py - пример управления автопилотом в локальных координатах
    * flight_global_test.py - пример управления автопилотом в глобальных координатах
    * led_test.py - пример управления светодиодами
    * logger_test.py - пример взаимодействия с логами
    * sensors_test.py - пример взаимодействия с бортовыми сенсорами
    * navigation_test.py - пример взаимодействия с системами навигации
    * cargo_test.py - пример взаимодействия с модулем магнитного захвата

2. Файлы запуска:
    * test_board.launch - пример запуска board_test
    * test_flight.launch - пример запуска flight_test
    * test_flight_global.launch - пример запуска flight_global_test
    * test_led.launch - пример запуска led_test
    * test_sensors.launch - пример запуска sensors_test
    * test_navigation.launch - пример запуска navigation_test

## Необходимые пакеты:
1. Python:
    * gs_board
    * gs_flight
    * gs_module
    * gs_logger
    * gs_sensors
    * gs_navigation
2. ROS:
    * gs_core
    * gs_interfaces

## Примечание:
Для работы всех нод, кроме cargo_test.py, необходима запущенная нода ros_plaz_node.py из пакета gs_core
cargo_test.py можно запустить:
```
python3 cargo_test.py
```