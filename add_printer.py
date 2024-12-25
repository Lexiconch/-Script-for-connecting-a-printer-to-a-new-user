import subprocess

def add_printer(printer_name, driver_name, port_name):
    try:
        # Создание порта
        subprocess.run([
            'powershell', '-Command',
            f'Add-PrinterPort -Name {port_name} -PrinterHostAddress "{port_name}"'
        ], check=True)

        # Добавление принтера
        subprocess.run([
            'powershell', '-Command',
            f'Add-Printer -Name "{printer_name}" -DriverName "{driver_name}" -PortName "{port_name}"'
        ], check=True)

        print(f'Принтер "{printer_name}" успешно добавлен.')

    except subprocess.CalledProcessError as e:
        print(f'Ошибка при добавлении принтера: {e}')

if __name__ == "__main__":
    # Задайте параметры принтера
    printer_name = "My_Printer"
    driver_name = "Microsoft Print To PDF"
    port_name = "192.168.1.100"

    add_printer(printer_name, driver_name, port_name)
