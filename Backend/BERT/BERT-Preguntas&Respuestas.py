# Importar
# mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es
# inigopm/beto-base-spanish-squades2
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
model = 'inigopm/beto-base-spanish-squades2'
tokenizer = AutoTokenizer.from_pretrained(model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(model)

# Ejemplo de inferencia (pregunta-respuesta)
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

from textwrap import wrap

def pregunta_respuesta(model, contexto, nlp):

  # Imprimir contexto
  print('Contexto:')
  print('-----------------')
  print('\n'.join(wrap(contexto)))

  #Loop preguntas-respuestas:
  continuar = True
  while continuar:
    print('\nPregunta:')
    print('-----------------')
    pregunta = input()

    continuar = pregunta != ''

    if continuar:
      salida = nlp({'question':pregunta,'context':contexto})
      print('\nRespuesta:')
      print('-----------------')
      print(salida['answer'])
      print('Con una certeza de:',salida['score'])

contexto ="""
La película empieza con una escena de la guerra contra las máquinas tras el "Día del Juicio Final" en el año dos mil veintinueve, donde Sarah Connor (Linda Hamilton) relata los acontencimientos contados en la película precedente y de como Skynet al fallar su plan ha decidido enfrentar a John siendo este aún un pequeño. Ahora, hay un salto a la actualidad de mil novecientos noventa y cinco. Un Terminator T-ochocientos (Schwarzenegger) llega desnudo por medio de un portal en el tiempo y entra a una cafetería para hurtar la ropa, el arma y la motocicleta a un motorista. En otra una parte de la urbe, otro Terminator desnudo que es el T-mil (Robert Patrick) se materializa y asesina a un agente de la ley para mimetizar su uniforme y hurtar su auto patrulla. Los dos empiezan a buscar a John Connor (Edward Furlong), ahora con diez años y que vive en la ciudad de Los Ángeles con sus progenitores adoptivos. John es muy rebelde y continuamente desacata a sus tutores, después de que su madre Sarah fuera detenida tras procurar bombardear una factoría de computadoras y está internada en el Centro de salud Siquiátrico de Pescadero, donde es atendida por el Doctor Silberman (Earl Boen).


El T-ochocientos y el T-mil hallan al tiempo a John en un centro comercial donde los dos pelean, siendo el T-ochocientos quien resguarda a John. Después John escapa en su moto del centro comercial y empieza una prosecución del T-mil, quien había robado un camion grúa hacia él mas en la mitad de todo llega el T-ochocientos y con gran habilidad lo salva de ser asesinado, consiguiendo evadir al T-mil por el momento. Los dos escapan en la moto del T-ochocientos.


Después de un tiempo de escapada John detiene al T-ochocientos y le solicita explicaciones. Este revela su identidad y le explica a un estupefacto John que es realmente una máquina proveniente del futuro, un autómata, modelo T-ochocientos que fue capturado y reprogramado por exactamente el mismo John en el futuro para resguardarlo en esa temporada, al tiempo le explica que el policía que estaba detrás de él tampoco es un humano, sino más bien un nuevo modelo de Terminator, un T-mil, mandado del futuro por Skynet, la supercomputadora consciente que lidera a las máquinas, para matar a John y con esto eludir su existencia, pues es el líder del conjunto rebelde llamado "La Resistencia", primordiales oponentes de Skynet. Asimismo le cuenta que el cuerpo del T-mil está hecho de metal líquido y puede tomar la manera de objetos afilados o bien otras personas al tocarlas.


El T-ochocientos se lleva a John lejos mas el chico insiste en pasar a su casa y recoger ciertas posesiones, el T-ochocientos se niega pues el T-mil podría estar aguardándolo. Sabiendo de la situación, John decide llamar a sus tutores para advertirles, no obstante cuando llaman el T-ochocientos (usando la voz de John) averigua con una patraña a la madre adoptiva de John y descubre conque el T-mil ya está en casa de John y ha asesinado a sus progenitores adoptivos. Entonces el T-ochocientos le revela que el próximo objetivo del T-mil va a ser matar a Sarah para tomar su forma y atraerlo a él, John al oír esto quiere salvarla de inmediato; no obstante, el T-ochocientos se niega aseverando que no es una parte de la misión. Se produce una discusión en la que el T-ochocientos levanta a John y este solicita ayuda, unos hombres asisten pensando que el T-ochocientos estaba hiriendo al joven, en ese instante John descubre que la máquina obedece sus órdenes por el hecho de que por él mismo lo programó para esto en el futuro, a modo de prueba John le ordena que ataque a los hombres, el T-ochocientos los reduce y también procura matar a uno de ellos mas John interviene y lo salva a último instante. La máquina le explica que iba a ejecutarlo en tanto que es un terminator, mas John le explica que no debe hacerlo, le ordena que ya no asesine a absolutamente nadie más y que vayan al Centro de salud Siquiátrico donde Sarah está internada para salvarla y los dos se dirigen cara allá.


En el centro de salud, el T-mil llega primero, mata a un guarda de seguridad y toma su forma yendo en busca de Sarah, al tiempo que en esos instantes Sarah con mucha habilidad consiguió salir de su celda y también procura escapar, tomando de rehén a su siquiatra, el doctor Silberman. Cuando es detenida por el resto médicos, el T-ochocientos y John llegan y salvan a Sarah, en ese instante aparece el T-mil, empieza un tiroteo y después una prosecución, mas consiguen escapar.




Esa noche se refugian en una estación de servicio y Sarah que fue herida en la prosecución por el T-mil es curada por el T-ochocientos, quien asimismo tiene conocimientos detallados y complejos de anatomía humana y medicina. Este le explica que su CPU está desarrollado para aprender más de los humanos y de este modo poder infiltrarse entre la gente más sencillamente y tener mayor probabilidad de éxito en su misión como terminator. Por la mañana siguiente escapan para adquirir comida y aprovisionar el vehículo en el que se desplazan. Sarah interroga al T-ochocientos de qué forma y en qué momento va a suceder "El Juicio Final", y este le explica sobre la creación de Skynet, por mano directa del doctor Miles Bennett Dyson (Joe Morton), ingeniero en jefe de Cyberdyne Systems, quien trabaja en un nuevo microprocesador, que va a ser la base de la creación de Skynet. Le cuenta que Skynet siendo iniciada, desarrollará autoconciencia transformándose en un ente inteligente que va a ver a los humanos como sus contrincantes, con lo que lanzará un ataque nuclear en torno a todo el planeta empezando con los rusos, que va a suceder en el mes de agosto de mil novecientos noventa y siete.


Sarah logra armas merced a Enrique Salceda (Castulo Guerra), un viejo amigo suyo que está en la frontera con México, planificando escapar entonces cara ese país. Después, Sarah tiene una pesadilla del ataque nuclear. Al despertar ve que ha escrito la oración "No Fate" (No hay destino), oración que Kyle Reese le había dicho, con lo que decide ir a matar a Miles Dyson para eludir el Día del Juicio Final. John trata de detenerla mas es inútil. Mientras que John y el Terminator sacan conclusiones, John se percata de que Sarah desea mudar el futuro matando a Dyson y va con el T-ochocientos a evitarlo, pese a las negativas de este, a sabiendas de que es una resolución tácticamente peligrosa pues posiblemente el T-mil haya adivinado sus pretensiones.


Esa noche, Sarah ataca a Dyson en su casa donde lo deja herido por un disparo, mas cuando está a puntito de matarlo al frente de su familia se percata de que no es capaz de hacerlo. John y el T-ochocientos llegan para evitarlo y John calma a Sarah. Entonces y para sorpresa de Dyson, el T-ochocientos le revela a este las consecuencias de su trabajo mostrándole que es un terminator. El científico, vomitivo con lo que ha escuchado, les explica que su trabajo se fundamentaba en los descubrimientos efectuados al estudiar el brazo y del chip del T-ochocientos que fue destruido por Sarah en mil novecientos ochenta y cuatro. Entonces decide abandonar a su trabajo, mas Sarah y el T-ochocientos le afirman que no es suficiente y que deben destruir todo registro de su trabajo de forma inmediata para eludir que en el futuro alguien lo siga.


Esa noche, se dirigen al edificio de Cyberdyne Systems para destruir todo el trabajo. John y Dyson recobran el brazo y el chip, mientras que el T-ochocientos y Sarah ponen bombas para destruir el laboratorio. Los policías son alertados por la seguridad de Cyberdyne y al llegar hieren de gravedad a Dyson, con lo que este se sacrifica y detona las bombas. Un equipo del SWAT llega, mas el T-ochocientos hiere a todos y birla el furgón del equipo con el que escapan. El T-mil llega tarde a la casa de Dyson, mas se entera por radio del ataque a Cyberdyne y parte cara el sitio. Ahí sigue persiguiéndolos en un helicóptero que birla a la policía, que al quedar destruido LO sustituye por un camión cisterna que transporta ázoe líquido y los persigue hasta una fundidora donde, producto de la colisión del camión, el ázoe líquido se desperdigada, congelando al T-mil mientras que procura continuar persiguiendo al conjunto, despedazándose parcialmente a resultas de no detenerse. El T-ochocientos lo descuartiza totalmente de un disparo, mas el calor de la fundidora lo devuelve a su estado líquido.


Luego de huir Sarah y John, los dos terminators pelean, mas el T-mil deja gravemente dañado al T-ochocientos y consigue desactivarlo al dañar su fuente primordial de energía clavándole una barra de metal en el abdomen. Más tarde se presenta en frente de John con la apariencia de Sarah, mas no consigue engañarlo, la auténtica Sarah confronta al T-mil incapacitándolo al dispararle sin cesar munición de alto poder y de esta manera eludir que se regenere mientras que los impactos lo empujan a caer en una caldera de metal derretido, por desgracia, ya antes de hacerlo caer las municiones de Sarah se agotan. A tiempo el T-ochocientos reinicia su sistema merced a su batería de urgencia y aparece para salvar a John, consiguiendo destruir al T-mil disparándole una bala explosiva que abre su abdomen, dejándolo en jirones de metal, cayendo al metal derretido a resultas del impacto, donde se funde tomando las formas de todas y cada una de las personas en que se convirtió hasta el momento en que no queda nada de él. John lanza el brazo y el chip al mismo sitio.


Sin embargo, el T-ochocientos les afirma que asimismo debe ser destruido a fin de que no quede otro chip y Skynet no sea creada, John le ruega que se quede, mas le afirma a John que no puede proseguir con ellos. Al ver plañir a John, consigue comprender su tristeza, mas le afirma que es una cosa que jamás va a poder hacer. Sarah angosta su mano, como agradecimiento por haber cumplido exitosamente su misión y por haber salvado la vida de John. Sarah lo baja al metal derretido y siendo destruido, el "Juicio Final" sería supuestamente eludido. La película acaba con Sarah contando que si un Terminator consiguió entender qué valiosa es la vida humana, tal vez algún día nosotros asimismo podamos hacerlo.
"""
pregunta_respuesta(model, contexto, nlp)