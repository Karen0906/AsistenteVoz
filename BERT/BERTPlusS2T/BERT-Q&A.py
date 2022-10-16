# Importar

from S2T import S2T
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# Obtener Modelo
# mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es
# inigopm/beto-base-spanish-squades2
model = 'inigopm/beto-base-spanish-squades2'
tokenizer = AutoTokenizer.from_pretrained(model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(model)

# NLP
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def pregunta_respuesta(contexto, nlp):

  #Loop preguntas-respuestas:
  while True:
    print('¿Qué pregunta quiere hacer?')
    pregunta = S2T()
    if pregunta != 'No speech detected ¡!¿?':
        return nlp({'question':pregunta,'context':contexto})['answer']
    else:
        return False

def pregunta_respuesta_inv(pregunta, nlp,ask=True):

  #Loop preguntas-respuestas:
  while True:
    if ask:
        print(pregunta)
    contexto = S2T()
    if contexto != 'No speech detected ¡!¿?':
        return nlp({'question':pregunta,'context':contexto})['answer']
    else:
        return False

def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

if __name__ == '__main__':
    while True:
        nombreU = pregunta_respuesta_inv('¿Cómo se llama?',nlp)
        while True:
            IdU = pregunta_respuesta_inv('¿Cual es su matrícula? (Solo número)',nlp)
            IdU = ''.join(IdU.split(' '))
            if checkInt(IdU):
                IdU = 'A'+IdU
                break
            else:
                print('Texto recibido contiene caracteres y no solo número, intente de nuevo...')

        print('Hola',nombreU + ', su matrícula es:', IdU + ', ¿Es la información ingresada correcta? (Diga si o no)')
        respuesta = pregunta_respuesta_inv('Sólamente dijo sí o no?',nlp,False).split(' ')[0]
        print(respuesta)
        if respuesta in ['si','sí']:
            break