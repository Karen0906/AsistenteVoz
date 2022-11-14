# Importar
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
model = 'finiteautomata/beto-sentiment-analysis'
tokenizer = AutoTokenizer.from_pretrained(model, do_lower_case=False)
model = AutoModelForSequenceClassification.from_pretrained(model)

# Ejemplo de inferencia (pregunta-respuesta)
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def returnFeedback(nlp,inputSen):
  while True:
    answer = nlp(input(inputSen))[0]['label']
    if answer == 'POS':
      return True
    elif answer == 'NEG':
      return False
    else:
      print('No entendimos su respuesta, intente de nuevo')

print(returnFeedback(nlp,'Escriba su comentario: '))