# Ejercicio: Fundamentos de Internet

## 1. Del Cliente al Servidor

Cuando escribo `www.youtube.com` en el navegador y presiono Enter, 
ocurre el siguiente proceso:

1. **El cliente (navegador)** hace una solicitud (request) para acceder 
   a youtube.com.

2. **El DNS (Domain Name System)** funciona como una guía telefónica: 
   traduce el nombre "youtube.com" a una dirección IP (un número), 
   porque las computadoras se comunican mediante números, no nombres.

3. **Con la dirección IP**, el navegador ya sabe dónde está el servidor 
   de YouTube y lo contacta.

4. **La comunicación usa HTTPS** (HTTP Secure), que encripta los datos 
   para que la conexión sea segura y la información no pueda ser 
   interceptada.

5. **El servidor** recibe la petición, la procesa (busca el contenido 
   solicitado) y envía una respuesta (response) de vuelta al navegador.

6. **El navegador** recibe la respuesta y muestra el contenido 
   (la página / el video) en pantalla.

## 2. Frontend y Backend

En una aplicación de citas médicas:

**Frontend** es la parte visual con la que interactúa el usuario 
(el paciente). Por ejemplo:
- La pantalla para elegir el doctor
- El calendario para seleccionar fecha y hora
- El formulario para ingresar sus datos
- El botón para agendar la cita

**Backend** es la parte interna que el usuario no ve. Se encarga 
de la lógica, los datos y el funcionamiento del sistema. Por ejemplo:
- La base de datos que almacena las citas, doctores y pacientes
- La lógica que verifica si un horario está disponible
- El envío de correos de confirmación
- La seguridad que protege la información médica

En resumen: el **frontend** es lo que el usuario ve y toca, mientras 
que el **backend** es el "cerebro" que procesa la información por 
detrás.