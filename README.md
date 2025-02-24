# Teorema de Bayes

Este programa permite gestionar fábricas de producción, ingresar probabilidades relacionadas con defectos en piezas producidas por cada fábrica, y calcular diversas probabilidades utilizando el teorema de Bayes. Además, ofrece la capacidad de añadir tantas fábricas como el usuario desee y realizar los cálculos correspondientes en tiempo real.

![Linux](https://github.com/user-attachments/assets/a3ba4d76-8f8b-443a-90d7-dd5e5d41916c)
![Windows](https://github.com/user-attachments/assets/bf2ffcf2-4078-446e-a830-f0bce79b4885)

## ⬇️ **Descarga del Proyecto**

Puedes descargar el programa tanto para **Linux** como para **Windows**. Los ejecutables los podrás encontrar en la sección de **Releases**!

## 🛠️ **Funcionalidades**

1. **Añadir fábricas**: El usuario puede añadir fábricas al sistema, especificando el nombre, el porcentaje de producción asignado y el porcentaje de piezas defectuosas en cada fábrica.
   
2. **Cálculos automáticos**: El programa realiza automáticamente los cálculos para obtener las siguientes probabilidades:
   - **P(D)**: Probabilidad global de piezas defectuosas.
   - **P(ND)**: Probabilidad de piezas no defectuosas.
   - **P(F|D)**: Probabilidad de que una pieza defectuosa provenga de una fábrica específica.
   - **P(F|ND)**: Probabilidad de que una pieza no defectuosa provenga de una fábrica específica.

3. **❌ Eliminación de fábricas**: El usuario puede eliminar fábricas del sistema con una confirmación de acción.

4. **⚙️ Manejo de probabilidades adicionales**: El programa permite agregar fábricas con más probabilidades como **P(E)** y **P(D|E)**, y calcular las probabilidades relacionadas con estas fábricas.

5. **💻 Interfaz de usuario amigable**: A través de una interfaz gráfica basada en `Qt`, el usuario puede interactuar fácilmente con las probabilidades, ver el estado de los cálculos y realizar modificaciones en las probabilidades de manera sencilla.

## 📚 **Uso**

1. **➕ Añadir fábricas**: Haz clic en el botón "Añadir fábrica" para abrir el cuadro de diálogo y añadir una nueva fábrica con sus respectivas probabilidades.
   
2. **✏️ Modificar probabilidades**: Las probabilidades de **P(Fábrica)** y **P(D|Fábrica)** se pueden modificar directamente desde la tabla. Los cálculos se actualizan automáticamente al modificar cualquiera de estos valores.

3. **🗑️ Eliminar fábricas**: Selecciona una fábrica en la tabla y haz clic en "Eliminar fábrica" para removerla del sistema.

4. **🔢 Cálculos de probabilidades**: El programa calcula las probabilidades automáticamente basándose en el teorema de Bayes. Los resultados de los cálculos se muestran en las columnas correspondientes de la tabla.

5. **💬 Configuración de Tooltips**: Los encabezados de las columnas contienen descripciones sobre cada tipo de probabilidad y su función, accesibles al pasar el ratón sobre ellos.

## 📂 **Archivos del Proyecto**

- **MainWindow.py**: El archivo principal que contiene la lógica de la interfaz y cálculos.
- **ui_form.py**: El archivo de interfaz de usuario generado con Qt Designer para la ventana principal.
- **ui_add_factory.py**: El archivo de interfaz de usuario generado con Qt Designer para el modal de adición.
- **AddFactoryDialog.py**: El archivo que define el diálogo para añadir fábricas.
- **PercentDelegate.py**: Clase que permite mostrar y editar los porcentajes de forma amigable.

