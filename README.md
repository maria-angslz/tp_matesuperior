# tp_matesuperior
tp de la materia matemastica superior. grupo mixto numero 9

## introduccion
El presente Trabajo Práctico, complementa las evaluaciones parciales de la asignatura, consiste en resolver un problema dado aplicando parte de los conceptos adquiridos en la segunda sección de la Materia, combinando técnicas algorítmicas o de programación de otras asignaturas para lograr de esta forma una integración horizontal. La forma/método y lenguaje de programación seleccionado para la resolución queda a decisión de cada grupo de alumnos, debiendo ellos analizar y evaluar diferentes estrategias y plataformas de desarrollo, tratando de ser eficientes en dicho proceso. De esta forma se desea lograr en los alumnos la capacidad de decidir el mejor camino a seguir ante un problema concreto. 

## forma de entrega 
 El trabajo deberá entregarse por mail al correo de Trabajos Prácticos, con en el siguiente formato:  1. Asunto: MatematicaSuperior_TP2C2018_[NombreGrupo] a. NombreGrupo: Nombre del grupo que figura en la planilla Excel en la grilla que se corresponde con su inscripción.  2. Archivo con el código fuente correspondiente al desarrollo del trabajo práctico, y de ser posible el ejecutable.  3. Archivo word que contenga el Manual de Usuario de la aplicación. 4. Correo de entrega: matematicasuperior.tp@gmail.com  
 
El desarrollo del trabajo debe garantizar su uso sin ninguna condición, es decir, que para utilizar la aplicación no se necesiten instalaciones adicionales más que el propio ejecutable.

## Fecha de Entrega 
 viernes 16 de noviembre 2018
 
 ## enunciado 
 
 El trabajo práctico consiste en el desarrollo de la aplicación SIEL (Sistemas de Ecuaciones Lineales) que permita procesar un sistema de ecuaciones lineales y obtener como resultado el conjunto de valores que satisfacen el sistema. 
 
 ### interfaz grafica (IG)
 
 IG representa la interfaz de usuario que contendrá la aplicación SIEL, la cual establecerá la ruta de comunicación entre el usuario y la aplicación. 
 
La interfaz gráfica deberá ser capaz de interpretar un lote de ecuaciones lineales definidas matricialmente como 𝐀 ∙ 𝐗 = 𝐁 siendo: A ∈ Rnxm la matriz de coeficientes, X ∈ Rmx1 la matriz columna de incógnitas y B ∈ Rnx1 la matriz columna de términos independientes.  
 
Como primera validación, SIEL analizará si la matriz de coeficientes es dominante diagonalmente/estrictamente dominante diagonalmente para luego informar al usuario que situación presenta el sistema cargado y brindar la posibilidad de modificar, si es necesario, el sistema hasta conseguir dicha característica.  
 
Adicionalmente brindará la posibilidad de obtener la Norma 1, Norma 2 y Norma Infinito de la matriz de coeficientes.   
 
Por último, se disponibilizarán los siguientes métodos iterativos para obtener la solución del sistema:  
* Método de Jacobi 
* Método de Gauss Seidel 
 
Al seleccionar el método se obtendrá el detalle de los pasos utilizados junto a la solución del mismo.  El usuario podrá:  Seleccionar otro método para resolver el mismo sistema.  Ingresar un nuevo sistema.  Salir de la aplicación.  

### Procesador de ecuaciones PE

El procesador de ecuaciones contendrá la lógica necesaria para interpretar cada una de las funcionalidades que brinda la interfaz de usuario. 
 
* Ingresar datos 
 
  La aplicación permitirá al usuario cargar el sistema de ecuaciones según el formato propuesto por el equipo de desarrollo. El objetivo es que la tarea de carga resulte ágil y simple de cara al usuario.  
 
* Seleccionar método para resolución 
 
  SIEL deberá ser capaz de interpretar el sistema seleccionado y ejecutar los pasos requeridos para brindar una solución. 
 
  Luego de seleccionar el método, tendrá que solicitar al usuario que ingrese:  
    * Vector inicial 
    * Cantidad de decimales 
    * Cota de error 
 
Como pasos de la resolución se visualizará por pantalla la tabla con todos los cálculos realizados como así también el criterio de paro utilizado. 
 
 * Seleccionar otro método 
 
SIEL otorgará al usuario la posibilidad de elegir resolver el sistema por otro método distinto al seleccionado originalmente. 
 
* Finalizar 
 
Con la opción finalizar, el usuario podrá terminar con todas las operaciones que estaba realizando para dar origen a un nuevo set de datos o incluso salir del programa.

## Manual de usuario  
 
Se deberá entregar junto al desarrollo del trabajo práctico, un manual de usuario el cual contenga por cada funcionalidad los pasos necesarios para dar con la respuesta esperada del sistema.   
 
Es importante considerar que este documento será el entregable final del trabajo realizado. 
