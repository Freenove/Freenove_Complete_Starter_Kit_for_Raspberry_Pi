using Microsoft.AspNetCore.Builder; using System.Device.Gpio;
var b=WebApplication.CreateBuilder(args); b.Services.AddSingleton<GpioController>(); var app=b.Build(); const int Led=18; var gpio=app.Services.GetRequiredService<GpioController>(); gpio.OpenPin(Led, PinMode.Output);
app.MapGet("/led/{s}", (string s)=>{ bool on=s.ToLower()=="on"; gpio.Write(Led, on?PinValue.High:PinValue.Low); return Results.Ok(new{led=on});});
app.Run("http://0.0.0.0:5000");