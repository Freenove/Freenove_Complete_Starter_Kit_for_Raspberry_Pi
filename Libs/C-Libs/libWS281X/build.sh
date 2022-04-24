#!/bin/sh
current_file=$0
cd "$(dirname "$current_file")"

arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c dma.c -o dma.o
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c mailbox.c -o mailbox.o
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c pcm.c -o pcm.o
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c pwm.c -o pwm.o
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c rpihw.c -o rpihw.o
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c ws2811.c -o ws2811.o
arm-linux-gnueabihf-g++ -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I. -I/usr/include/python3.7m -c Freenove_WS2812_Lib_for_Raspberry_Pi.cpp -o Freenove_WS2812_Lib_for_Raspberry_Pi.o

sudo arm-linux-gnueabihf-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2  dma.o mailbox.o  pcm.o pwm.o rpihw.o ws2811.o Freenove_WS2812_Lib_for_Raspberry_Pi.o -o libWS281X.so

sudo cp clk.h dma.h gpio.h mailbox.h pcm.h pwm.h rpihw.h ws2811.h Freenove_WS2812_Lib_for_Raspberry_Pi.hpp  /usr/include/
sudo cp libWS281X.so /usr/lib/
sudo ldconfig

echo "build completed!"
