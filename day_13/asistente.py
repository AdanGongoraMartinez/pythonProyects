import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

from gtts import gTTS
import os

# escuchar microfono y devolver el audio como texto
def trasformar_audio_a_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('ya puedes hablar')

        # guardar lo que escuches como audio
        audio = r.listen(origen)

        try:
            # buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de ingreso
            print("Digiste: "+pedido)

            # devolver pedido
            return pedido
        
        # no comprender el audio
        except sr.UnknownValueError:
            
            # prueba de no comprension
            print("No entendi :c")

            # devolver error
            return "Sigo esperando"
        
        # no poder resolver el pedido
        except sr.RequestError:
            # prueba de no comprension
            print("No hay servicio :c")

            # devolver error
            return "Sigo esperando"

        # error inseperado
        except Exception as e:
            # prueba de no comprension
            print("Excepcion: ", e)

            # devolver error
            return "Sigo esperando"


# funciona para que el asistente hable
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', 'spanish-latin-am')

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


def speak(text):
    # Passing the text and language to the engine, slow=False to make the speech slower
    tts = gTTS(text=text, lang='es', tld='com.mx')

    # Saving the converted audio in a file named sample.mp3
    tts.save("sample.mp3")
    print(f'Mensaje: {text} - gurdado')

    # Playing the converted file
    os.system("mpg321 sample.mp3")


# informar el dia de la semana
def pedir_dia():
    # datos de hoy
    dia = datetime.date.today()

    # crear variable para el dia de semana
    dia_semana = dia.weekday()

    #d diccionario dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # decir el dia de la semana
    return f'Hoy es {calendario[dia_semana]}'


# informar hora
def pedir_hora():
    
    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)

    # decir la hora
    return f'En este momento son las {hora.hour} horas con {hora.minute} minutos.'


# saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # decir el saludo
    return f"{momento},soy tu asistente personal. Por favor, dime en qué te puedo ayudar"


# funcion central del asistente
def pedir_cosas():
    # activar saludo inical
    speak(saludo_inicial())

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = ''
        pedido = trasformar_audio_a_texto().lower()

        if 'abre youtube' in pedido:
            speak('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abre el navegador' in pedido:
            speak('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue

        elif 'qué día es hoy' in pedido:
            speak(pedir_dia())
            continue

        elif 'qué hora es' in pedido:
            speak(pedir_hora())
            continue

        elif 'busca en wikipedia' in pedido:
            speak('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)

            speak(f'Wikipedia dice lo siguiente: {resultado}')

            continue

        elif 'busca en internet' in pedido:
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue

        elif 'reproducir' in pedido:
            speak('Ya comienzo a reproducirlo')
            pedido = pedido.replace('reproducir','')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            speak(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].split()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                speak(f'La encontré, el precio de {accion} es {precio_actual}')
            except:
                speak('Perdon, no la he encontrado')

            continue

        elif 'adiós' in pedido:
            speak("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()