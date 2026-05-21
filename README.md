ScholarReviews

ScholarReviews es una plataforma web donde los usuarios pueden compartir reseñas de libros, expresar su opinión y descubrir nuevas lecturas a través de las experiencias de otras personas.

El objetivo principal del proyecto es crear un espacio interactivo y accesible para fomentar la lectura, el aprendizaje y el intercambio de ideas entre estudiantes y lectores.

CARACTERÍSTICAS PRINCIPALES
Registro e inicio de sesión de usuarios
Inicio de sesión con Google
Publicación de reseñas de libros
Edición y eliminación de reseñas propias
Sistema de likes y comentarios
Visualización de perfiles de usuarios
Búsqueda de publicaciones y usuarios
Clasificación por categorías educativas
Cambio de idioma (Español/Inglés)
Modo oscuro y modo claro
Integración con OpenLibrary API
Almacenamiento de imágenes con Cloudinary
Base de datos en Supabase


Tecnologías utilizadas 🛠️
<p align="left"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/supabase/supabase-original.svg" width="40"/> </p>


Instalación y configuración 
1. Clonar el repositorio
git clone https://github.com/USUARIO/ScholarReviews.git
cd ScholarReviews
2. Crear entorno virtual
python -m venv env

<b>Activar entorno virtual:</b>
env\Scripts\activate

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar variables de entorno
Crear un archivo .env en la raíz del proyecto y agregar:

SECRET_KEY=clave_secreta

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

5. Aplicar migraciones
python manage.py migrate
Registro de usuario<br>
6. Ejecutar el servidor
python manage.py runserver

Registro de usuario
<img width="700" alt="image" src="https://github.com/user-attachments/assets/1f1f436c-2bba-4087-87f2-e7ef6d6cd2e4" />

Página principal
<img width="700" alt="image" src="https://github.com/user-attachments/assets/871ce1ce-d489-40c9-b30e-331945569492" />

Crear reseña<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/a562f259-486c-48f3-aa97-613babacfaa7" />

Perfil<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e1e4202d-002a-49c3-9aab-249fc76cc0c1" />


Estructura del proyecto 📂

ScholarReviews/
│
├── app/
├── mysite/
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md




Equipo de desarrollo

Castillo Lopez Julio Cesar <br>
Frías Rodríguez Nelvin Antonio<br>
Navarro Suárez Keyla Cecilia<br>
Rodríguez Hernandez Xanic Osmelí<br>
Ruíz Ríos Jonás Eloy<br>

Licencia 

Este proyecto fue desarrollado con fines educativos.
