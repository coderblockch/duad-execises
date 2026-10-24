# Fundamentos de Internet

**Autor:** Jorge David Jiménez
**Módulo:** El Internet — Internet, HTTP y APIs

---

## 1. Del Cliente al Servidor

Cuando escribo `www.youtube.com` en el navegador y el video aparece en pantalla, ocurre lo siguiente paso a paso:

1. **El cliente (navegador) inicia la solicitud.** Yo escribo la URL y el navegador la interpreta. Primero revisa su **caché** (si ya visitó el sitio antes); si no tiene la dirección guardada, necesita averiguar a qué servidor conectarse.

2. **El DNS traduce el nombre a una dirección IP.** El nombre `www.youtube.com` es fácil de recordar para las personas, pero las computadoras se comunican por números. El **DNS (Domain Name System)** funciona como la "agenda de contactos" de internet: traduce el nombre del dominio a su **dirección IP** (por ejemplo, `142.250.72.206`).

3. **Con la IP, el navegador contacta al servidor.** Ya sabiendo la dirección IP, el navegador abre una conexión con el servidor de YouTube. Se establece primero una conexión **TCP** (el "apretón de manos" que asegura que ambos lados están listos).

4. **Se asegura la conexión con HTTPS.** Como YouTube usa **HTTPS**, se realiza además un **handshake TLS**, que cifra la comunicación. Así, los datos que viajan entre mi navegador y el servidor van **encriptados** y protegidos. (Ese es el paso de pasar de HTTP a **HTTPS**: la "S" es de *Secure*.)

5. **El navegador envía la petición HTTP.** El navegador manda una **solicitud (request)** del tipo `GET` pidiendo la página. La solicitud incluye *headers* con información (idioma, tipo de navegador, etc.).

6. **El servidor procesa y responde.** El servidor de YouTube recibe la petición, la procesa y devuelve una **respuesta (response)** con un **código de estado** (por ejemplo `200 OK`) y el contenido: el HTML, CSS y JavaScript de la página.

7. **El navegador renderiza y carga el video.** El navegador arma la página visual y hace **solicitudes adicionales** para cargar el video (que llega por *streaming*, en pedacitos). Finalmente, el video aparece en pantalla. 🎬

### Diagrama del flujo

```
  [ CLIENTE ]                [ DNS ]                 [ SERVIDOR ]
  Navegador                                          YouTube
     |                                                   |
     | 1. ¿Cuál es la IP de www.youtube.com?             |
     |-------------------->  [ DNS ]                      |
     |                         |                          |
     | 2. IP: 142.250.72.206   |                          |
     |<--------------------    |                          |
     |                                                    |
     | 3. Conexión TCP + TLS (HTTPS)                      |
     |-------------------------------------------------->  |
     |                                                    |
     | 4. HTTP Request:  GET /                            |
     |-------------------------------------------------->  |
     |                                                    |
     | 5. HTTP Response: 200 OK + HTML/CSS/JS + video     |
     |<--------------------------------------------------  |
     |                                                    |
   [ Se renderiza la página y el video aparece ]
```

---

## 2. Frontend y Backend en acción

Para una app web de **agendar citas médicas**:

El **frontend** es la parte visual con la que interactúa el usuario: el formulario para elegir médico, el calendario para seleccionar fecha y hora, los botones para confirmar. Es todo lo que el paciente ve y toca en la pantalla.

El **backend** es la parte interna que el usuario no ve: se encarga de la lógica del sistema, la **base de datos** donde se guardan las citas y los pacientes, las validaciones (que no se agende una hora ocupada) y el armado de las respuestas.

### Tecnologías posibles

| Capa | Tecnologías |
|------|-------------|
| **Frontend** | HTML/CSS, JavaScript, React (también Vue o Angular) |
| **Backend** | Python con Flask, Node.js, o Java con Spring |

### ¿Cómo se comunican?

El frontend y el backend se comunican a través de una **API**. Cuando el paciente confirma una cita, el frontend envía una **solicitud (request) HTTP** a la API del backend —por ejemplo, un `POST /citas` con los datos de la cita en formato JSON—. El backend recibe esa petición, la procesa, guarda la cita en la base de datos y devuelve una **respuesta (response)** con un código de estado (como `201 Created`) confirmando que la cita se agendó. Ese ciclo de ida y vuelta es el **request/response**.

---

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual |
|-------------|------------------------|------------------------|------------------------------|------------|
| **REST** | JSON (a veces XML) | Media — el servidor define los endpoints y qué devuelve cada uno | Baja — fácil de aprender, muchísimas herramientas | **Alta** |
| **SOAP** | XML (estricto, con contrato WSDL) | Baja — contrato rígido, poco margen de cambio | Alta — verboso, pesado, más difícil de mantener | **Baja** (sistemas legados: banca, gobierno) |
| **GraphQL** | JSON (con lenguaje de consultas propio) | Alta — el **cliente** pide exactamente los datos que necesita, ni más ni menos | Media — tiene curva de aprendizaje y requiere configuración | **Media** (en crecimiento) |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

Para una startup que desarrolla un sistema de reservas en línea, considero más apropiada **REST**. Las razones:

- Es **fácil y rápida de implementar**, lo que le permite a la startup salir al mercado pronto (clave cuando el tiempo y el dinero son limitados).
- Tiene una **comunidad enorme** y muchísimas herramientas (como Postman), lo que facilita el desarrollo y el mantenimiento.
- El formato **JSON** es ligero y fácil de manejar tanto en el frontend como en el backend.

GraphQL sería una buena opción más adelante, si la app crece y necesita manejar muchas vistas con datos muy variables (por ejemplo, apps móviles que piden datos distintos según la pantalla). SOAP lo descartaría: es pesado y se usa sobre todo en sistemas antiguos.

---

## 4. Explorando APIs con Postman

### 4.1 Selección de la API

- **Nombre de la API:** JSONPlaceholder (`https://jsonplaceholder.typicode.com`)
- **Descripción:** Es una API REST pública y gratuita, **sin autenticación**, pensada para practicar y hacer prototipos. Simula los datos de un blog (posts, comentarios, usuarios, tareas). La elegí porque, a diferencia de APIs de solo lectura como PokéAPI, **permite probar los cuatro métodos** (GET, POST, PUT y DELETE), que es justo lo que pide el ejercicio.

### 4.2 Configuración en Postman

- **Nombre de la colección:** JSONPlaceholder
- **Solicitudes agregadas:**
  - **GET** — `https://jsonplaceholder.typicode.com/posts/1` (obtener un post)
  - **POST** — `https://jsonplaceholder.typicode.com/posts` (crear un post)
  - **PUT** — `https://jsonplaceholder.typicode.com/posts/1` (actualizar un post)
  - **DELETE** — `https://jsonplaceholder.typicode.com/posts/1` (eliminar un post)

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint | Código de estado | Notas |
|-----------|--------|----------|------------------|-------|
| Obtener un post | GET | `/posts/1` | `200 OK` | Devuelve un post en formato JSON |
| Crear un post | POST | `/posts` | `201 Created` | Devuelve el nuevo recurso con `id: 101` |
| Actualizar un post | PUT | `/posts/1` | `200 OK` | Devuelve el objeto ya actualizado |
| Eliminar un post | DELETE | `/posts/1` | `200 OK` | Devuelve un objeto vacío `{}` |

*Header relevante en todas las respuestas:* `Content-Type: application/json; charset=utf-8`

### 4.4 Explicación técnica

**JSONPlaceholder** es una API de prueba que responde como si fuera un backend real de un blog, pero sin guardar los cambios de verdad (los simula). Esto la hace ideal para aprender cómo viajan las peticiones y respuestas.

#### Obtener un post (GET)

- **Método HTTP:** GET
- **Endpoint:** `/posts/1`
- **Parámetros / body:** No lleva body. El `1` en la ruta es el id del post que pido.
- **Descripción de la respuesta:** Devuelve los datos del post con id 1.

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur..."
}
```

#### Crear un post (POST)

- **Método HTTP:** POST
- **Endpoint:** `/posts`
- **Parámetros / body:** En el body envío el nuevo post en JSON:

```json
{
  "title": "Mi primer post",
  "body": "Estoy aprendiendo APIs con Postman",
  "userId": 1
}
```

- **Descripción de la respuesta:** Devuelve el recurso creado con un `id` nuevo (101) y estado `201 Created`.

```json
{
  "title": "Mi primer post",
  "body": "Estoy aprendiendo APIs con Postman",
  "userId": 1,
  "id": 101
}
```

#### Actualizar un post (PUT)

- **Método HTTP:** PUT
- **Endpoint:** `/posts/1`
- **Parámetros / body:** El objeto completo con los datos actualizados.
- **Descripción de la respuesta:** Devuelve el post con los cambios aplicados, estado `200 OK`.

#### Eliminar un post (DELETE)

- **Método HTTP:** DELETE
- **Endpoint:** `/posts/1`
- **Parámetros / body:** No lleva body.
- **Descripción de la respuesta:** Devuelve un objeto vacío `{}` con estado `200 OK`, indicando que el recurso fue eliminado.

**¿Qué aprendiste del proceso?**

Aprendí que cada método HTTP tiene un propósito claro: GET para **leer**, POST para **crear**, PUT para **actualizar** y DELETE para **eliminar**. También que el **código de estado** de la respuesta me dice rápidamente qué pasó (200 = todo bien, 201 = se creó, 404 = no encontrado), y que los datos viajan en formato **JSON**.

### 4.5 Reflexión final

Con este ejercicio entendí que una **API** es como un mesero entre el cliente (frontend) y la cocina (backend): yo hago un pedido (request) con un método y un endpoint, y recibo una respuesta (response) con datos y un código de estado. Cada método HTTP cumple una función distinta dentro del ciclo de comunicación, y todo viaja de forma ordenada gracias al protocolo HTTP.

**Postman** me ayudó muchísimo a *ver* esa comunicación de manera concreta: pude enviar peticiones reales sin necesidad de programar una interfaz, revisar el código de estado, leer el cuerpo de la respuesta en JSON y entender los headers. Fue como tener una ventana directa a la conversación entre el cliente y el servidor, lo que me dio una idea mucho más clara de cómo funcionan por dentro las aplicaciones web que uso todos los días.
