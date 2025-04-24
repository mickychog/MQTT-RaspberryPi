<a name="readme-top"></a>
![Maintained][Maintained-shield]
![Forks][Forks-shield]
![Pull Request][PullRequest-shield]
![Pull Request Closed][PullRequestclosed-shield]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mickychog/MQTT-RaspberryPi">
    <img src="assets/rasp.png" alt="Logo" width="275" height="183">
  </a>

<h3 align="center">MQTT Communication</h3>

  <p align="center">
    MQTT server that handles robotics actions in the raspberry
    <br />
    <a href="https://github.com/mickychog/MQTT-RaspberryPi/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/mickychog/MQTT-RaspberryPi/issues">Report Bug</a>
    ·
    <a href="https://github.com/mickychog/MQTT-RaspberryPi/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyeto">Acerca Del Proyeto</a>
    </li>
    <li><a href="#hardware-necesario">Hardware Necesario</a></li>
    <li><a href="#configuracion-de-entorno">Configuracion de entorno</a></li>
    <li>
      <a href="#descarga">Descarga</a>
    </li>
    <li><a href="#instalacion">Instalacion</a></li>
    <li><a href="#configuracion-del-proyecto">Configuracion del proyecto</li>
    <li><a href="#tech-stack">Tech Stack</a></li>
  </ol>
</details>

## Acerca Del Proyeto

`MQTT Communication` es un proyecto basico Open Source que permite crear la comunicacion entre un host MQTT y cualquier otro host mediante el protocolo MQTT permitiendo la comunicacion mediante el patron MQTT.

Este es un inicio basico para trabajar con Python usando un publicador y un suscriptor

- EL protocolo MQTT permite crear un topico por el cual se comunican mediante el mismo topico, esto para enviar mensajes
- El `Payload` resulta tan ligero que es posible realizar proyectos de domotica

## Hardware Necesario

> [!IMPORTANT]
> El `Hardware` necesario para este proyecto dependera de la implementacion del usurio, en este caso el proyecto de ejemplo solo usara un led para hacer `testing` del protocolo

- Raspberry pi
- 3 Leds
- 3 Resistencias
- Jumpers

## Configuracion de entorno previa

Considerando que el proyecto hace uso de los pines `GPIO` es importante instalar y configurar las dependencias relacionadas a esta para tenerlas activas en todo momento

```
$ sudo apt update
$ sudo apt install -y pigpio pthon3-pigpio
$ sudo systemctl enable pigpiod
$ sudo systemctl start pigpiod
```

## Descarga

```
$ git clone https://github.com/NicoZela23/CV-Robotic-Claw.git
$ cd MQTT-RaspberryPi
$ python -m venv clawENV
$ source clawENV/bin/activate
```

## Instalacion

El proyecto no requiere de una instalacion mas alla de la ejecucion del script de Python, en este caso el archivo `mqtt_sub` debera ser ejecutado en el `Raspberry` y el archivo `mqtt_pub` en cualquier otro host que hara la comunicacion

```
$ sudo python mqtt_sub.py
```

Y el otro archivo dependera del entorno de ejecucion sin envargo el resultado sera el mismo al solo tenere que ejecutar el script

## Configuracion del proyecto

La base del proyecto es para encender y apagar leds con comandos enviados desde el host publicador sin embargo al estar usando los pines `GPIO` esto puede ser aplicado a cualquier implementacion de robotica

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![Debian](https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=fff)]()

[Maintained-shield]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[Forks-shield]: https://img.shields.io/github/forks/mickychog/MQTT-RaspberryPi.svg
[PullRequest-shield]: https://img.shields.io/github/issues-pr/mickychog/MQTT-RaspberryPi.svg
[PullRequestclosed-shield]: https://img.shields.io/github/issues-pr-closed/mickychog/MQTT-RaspberryPi.svg
[Java]: https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white
[Java-url]: https://www.java.com/es/
[IntelliJ]: https://img.shields.io/badge/Intellij%20Idea-000?logo=intellij-idea&style=for-the-badge
[IntelliJ-url]: https://www.jetbrains.com/idea/
[Git]: https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com/
[Powershell]: https://img.shields.io/badge/powershell-5391FE?style=for-the-badge&logo=powershell&logoColor=white
[Powershell-url]: https://www.microsoft.com/store/productId/9MZ1SNWT0N5D?ocid=pdpshare
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[Github-url]: https://github.com/
