using Iot.Device.FtCommon;

try
{
    var devices = FtCommon.GetDevices();
    Console.WriteLine($"{devices.Count} available device(s)");
    foreach (var device in devices)
    {
        Console.WriteLine($"  {device.Description}");
        Console.WriteLine($"    Flags: {device.Flags}");
        Console.WriteLine($"    Id: {device.Id}");
        Console.WriteLine($"    LocId: {device.LocId}");
        Console.WriteLine($"    Serial number: {device.SerialNumber}");
        Console.WriteLine($"    Type: {device.Type}");
    }

    if (devices.Count == 0)
    {
        Console.WriteLine("No device connected");
        return;
    }
}
catch(Exception ex)
{
    Console.WriteLine($"Exception: {ex.Message}");
    return;
}