
param (
    [string]$PrinterName = "My_Printer",
    [string]$DriverName = "Microsoft Print To PDF",
    [string]$PortName = "192.168.1.100"
)

try {
    # Создание порта
    Write-Host "Создание порта: $PortName"
    Add-PrinterPort -Name $PortName -PrinterHostAddress $PortName

    # Добавление принтера
    Write-Host "Добавление принтера: $PrinterName"
    Add-Printer -Name $PrinterName -DriverName $DriverName -PortName $PortName

    Write-Host "Принтер '$PrinterName' успешно добавлен."
} catch {
    Write-Host "Ошибка при добавлении принтера: $_"
}
