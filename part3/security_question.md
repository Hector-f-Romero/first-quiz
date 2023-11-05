# Implementando OWASP Top 10 2021 🤔

De acuerdo al contexto brindado anteriormente, la forma de abordar los puntos más importantes de cada item del OWASP Top 10 2021 para lograr que el sistema sea más seguro sería la siguiente:

## 1. Broken Access Control - Control de acceso remoto

Analizar si es necesario que los doce ingenieros de software deban tener acceso total al sistema y a la información que este requiere. Después de esto, es necesario revisar las políticas de control de acceso para asegurar de que solo los usuarios autorizados puedan acceder a funciones sensibles (desencriptación de información en la base de datos principalmente). Si no es necesario que todos estos ingenieros puedan acceder a los sistemas más sensibles de la empresa, se le asignaría a un pequeño número de trabajadores las credenciales necesarias y que estas no sean expuestas en ningún momento dentro del frontend, backend y base de datos

## 2. Cryptographic Failures - Fallas Criptográficas

Verificar que los métodos para cifrar la información posean algortimos de hash seguros y salting. Si estos algortimos son provistos por librerías externas como `bcrypt` o similares, se requerirá comprobar si la versión es estable y no posee fallos de seguridad mientras se esté usando dentro del sistema. Además, será necesario decidir que información de la base de datos debe ser encriptada y cuál no, buscando preever la fácil traducción de esta.

Por otro lado, mientras se estén comunicando los diferentes microservicios del sistema, es de vital importancia comprar que los datos enviados estén cifrados para evitar intercepciones maliciosas.

## 3. Injection - Inyección

Principalmente la acción a tomar en este apartado será verificar la defensa del sistema frente a diferentes intentos de inyecciones de SQL y similares, buscando generar validaciones más estrictas al momento de hacer operaciones en la BD. De estar empleando un ORM, será necesario buscar la forma en cómo este puede evitar este tipo de ataques.

## 4. Insecure Design - Diseño Inseguro

Implementar patrones de diseños seguros, limitar el consumo de recursos que el usuario puede emplear desde la página web o app y asesorarse con profesionales en la ciberseguridad son algunos elementos a considerar para atender a este apartado.

## 5. Security Misconfiguration - Configuración de Seguridad Incorrecta

Se deberá echar ojo sobre las funciones y usuarios innecesarios que no se han eliminado completamente como lo pueden ser páginas de pruebas de Next descartadas, usuarios con privilegios empleados para pruebas entre los ingenieros de software, entre otras. Además de eso, inspeccionar los encabezados de las peticiones HTTP y buscar que no expongan información sensible serán otras tareas a tener en cuenta en este apartado. Por último, cuando se le muestren errores al usuario por medio de interfaces, será de vital importancia analizar si el manejo de errores revela a los usuarios rastros de pila u otros mensajes de error demasiado informativos, ya que este puede ser el pie de entrada para la realización de muchos ataques.

## 6. Vulnerable and Outdated Components - Componentes Vulnerables y Desactualizados

Como equipo de trabajo, es necesario verificar que el software utilizado uilice versiones recientes y estables que no poseean fallos de seguridad (si se utilizan versiones LTS de los programas, verificar hasta cuándo darán soporte a dicha versión). Asimismo, será importante que se compruebe rigurosamente la compatibilidad entre librerias y frameworks al momento de actualizarlos antes de llevarse a producción, pues de no hacerse puede generar errores en cualquiera de los servicios.

## 7. Identification and Authentication Failures - Fallas de Identificación y Autenticación

Para abordar este apartado, será necesario fortalecer los mecanismos de autenticación que pueden usar los usuarios y asegurarse de que la gestión de sesiones sea segura para prevenir ataques como la toma de sesión o la suplantación de identidad. Implementar la autenticación multi-factor puede poner freno a los ataques automatizados y no almacenar información sensible que pueda ser accesida fácilmente desde el cliente (por ejemplo, no guardar tokens inseguros o información delicada en `localstorage`).

## 8. Software and Data Integrity Failures - Fallas en el Software y en la Integridad de los Datos

Asegurarse de que el código y los datos no se vean comprometidos en cualquier punto del sistema. Para lo cual, utilizar firmas digitales y verificar que el pipeline CI/CD posee adecuados controles de acceso, segregación y configuraciones que permitan asegurar la integridad del código a través del proceso de build y despliegue serán formas efectivas de prevenir estas fallas.

## 9. Security Logging and Monitoring Failures - Fallas en el Registro y Monitoreo

Será necesario implementar un sistema de registro y monitoreo cuando el usuario comete errores al iniciar sesión, control de acceso y validación de entradas, pues de esta forma será más sencillo identificar de mejor manera actividades sospechosas o maliciosas. Estos registros no deberán guardarse únicamente de forma local para evitar pérdida de información o no alertar a demás microservicios de forma temprana.

## 10. Server-Side Request Forgery (SSRF) - Falsificación de Solicitudes del Lado del Servidor (SSRF)

Por último, es importante que los entornos de AWS y el backend de Python hayan sido construido para estar protegido contra SSRF, donde un atacante podría aprovechar SSRF para acceder a servicios internos. Usar cifrado de red cuando se comunican las aplicaciones móviles con el backend, evitar redirecciones HTTP son medidas para atender ante esta falla.
