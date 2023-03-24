


import pandas as pd
from matplotlib import pyplot as plt




### Leer la base de datos de lirios
df=pd.read_csv('iris.csv')


# ### Código 




def analisis_general(df):
  print('Número Total de Atributos:' + str(df.shape[1]))
  print('')
  for column in df:
    print('Nombre de la columna: ', column)
    print('Contenido de la columna: ', df[column].values)
    print('')
    #Observaciones de cada Atributo
    Lists = [] #Creación de una lista
    Tipo = []
   
    for List in df[column].values: #Recorrer los valores de la columna en cuestión
      if List not in Lists: #Si el valor no se encuentra en la lista
        Lists.append(List) #Agregar a la lista ese valor
    # print('Observaciones de los Atributos:',Lists)  
    print('')

    
  #Número de Instancias
  print('Número de Instancias por Atributo:' + str(df.shape[0]))
  print('')
  print('Tipo de Atributo')
  print(df.dtypes)
  #Valores Faltantes (Porcentaje)
  print(' -----------------------------------------------------------------')
  print('')
  Porcentaje_NaN = ((df.isnull().sum() / len(df))*100).sort_values(ascending = False)
  print('Porcentaje de Valores Faltantes')
  print(Porcentaje_NaN)
  print('')





def cov(df,columnas):
  y=z=0
  copy = df.copy()
  for column in copy: #Recorrer la columnas de la copia del dataset
    for col in columnas: #Recorrer las valores de la lista de columnas
        #Si los valores de las columnas entre la copia del dataset y la lista de columnas no concide
        if column != col: 
          copy.drop(col, axis=1) #Eliminar de la copia del dataset la columna en cuestión

  for index in range(copy.shape[1]): #Recorrer las posiciones de las columnas de la copia del dataset
   #Considerar unicamente las columnas sin valores de tipo string
    if copy.iloc[:,index].dtypes == 'float64'or copy.iloc[:,index].dtypes == 'int64' :
        index1= index + 1
        #Diferencia entre el valor de z y su promedio, en donde el valor obtenido se dividira entre el total de las filas del dataset
        y = (copy.iloc[:,index] - ((sum(copy.iloc[:,index]))/len(copy)))
        for index1 in range(copy.shape[1]): #Recorrer las posiciones de las columnas de la copia del dataset
          if copy.iloc[:,index1].dtypes == 'float64'or copy.iloc[:,index].dtypes == 'int64': #Considerar unicamente las columnas sin valores de tipo string
            z = (copy.iloc[:,index1]- ((sum(copy.iloc[:,index1]))/len(copy))) #Diferencia entre el valor de z y su promedio, en donde el valor obtenido se dividira entre el total de las filas del dataset
            c = sum(y*z)/len(copy) # Formula para la covarianza
           # print('Covarianza de la columna',columnas[index], 'y la columna', columnas[index1],':', c)   quitar
  print('')


# In[5]:


 
def sta_atributos1(df):
    print(' -----------------------------------------------------------------')
    print('')
    columnas = []
    
    for column in df:
        if df[column].dtypes == 'float64' or df[column].dtypes == 'int64':
            columnas.append(column)
            
            # Agregar cálculos de estadísticas descriptivas
            print('Estadísticas descriptivas para', column)
            print('Media:', df[column].mean())
            print('Moda:', df[column].mode()[0])
            print('Valor Mínimo:', df[column].min())
            print('Valor Máximo:', df[column].max())
            print('Desviación Estándar:', df[column].std())
            print('')
# Agregar histograma
        plt.hist(df[column])
        plt.title(column)
        plt.show()
        if df[column].dtypes == 'object':
            print('Frecuencia de valores para', column)
            print(df[column].value_counts())
            print('')
            columnas.append(column)
            # Agregar gráfica de barras
            plt.bar(df[column].value_counts().index, df[column].value_counts())
            plt.title(column)
            plt.show()    
    return columnas

def clasif(df, col_clasif):
    """
    Clasifica los datos en el DataFrame proporcionado según la columna de clasificación especificada.

    Parameters:
    -----------
    df: DataFrame
        El DataFrame que contiene los datos a clasificar.

    col_clasif: str
        El nombre de la columna que se utilizará para clasificar los datos.

    Returns:
    --------
    None
    """
    print('Clasificación de los datos por:', col_clasif)
    print('-------------------------------------------')
    print(df[col_clasif].value_counts())




def FG(df,Col_clasif):
  analisis_general(df)
  sta_atributos1(df)
  clasif(df,Col_clasif)


#Establecer la columna para realizar el balance de clases
Col_clasif = 'Lirio'
columnas = FG(df,Col_clasif)


# ### Comparación

# In[12]:

#Estadistica
df.describe()

