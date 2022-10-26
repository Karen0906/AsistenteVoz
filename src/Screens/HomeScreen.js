import React from 'react';
import Card from 'react-bootstrap/Card';

function HomeScreen() {

  return (
    <div class='container'>
      <div class='hero-unit'>
        <h1 class= 'mt-5' style={{color: '#121B4F'}}> Conmutador a asistentes de voz</h1>
        <p style={{color: '#47525E'}}>El nuevo sistema de conmutación automatizado que sea capaz de conectarse a varios motores conversacionales y seleccionar el mejor de acuerdo a la entrada del usuario</p>
        <p>
        </p>
      </div>
      <div class='row gx-3 mt-5 align-center'>
        <div class='col-auto'>
          <Card style={{ width: '15rem', height:'14rem', borderColor:'#f9e401', borderWidth:'4px'}}>
                <Card.Body>
                  <Card.Title style={{color: '#121B4F'}}>1. Selecciona</Card.Title>
                  <Card.Text mb-3 style={{color: '#47525E'}}>
                    Las preguntas que más se relacionen a tu negocio, importa documentos csv, añade y edita lo que necesites. 
                  </Card.Text>
                </Card.Body>
              </Card>
              <br />
        </div>
        <div class='col-auto'>
            <Card style={{ width: '15rem', height:'14rem', borderColor:'#f9e401', borderWidth:'4px'}}>
                  <Card.Body>
                    <Card.Title style={{color: '#121B4F'}} >2. Aporta</Card.Title>
                    <Card.Text mb-3 style={{color: '#47525E'}}>
                      Los documentos, respuestas o información relevante relacionada a las preguntas previamente elegidas.
                    </Card.Text>
                  </Card.Body>
                </Card>
                <br />
        </div>
  {/* <div class='w-100'></div> */}
        <div class='col-auto'>
        <Card style={{ width: '15rem', height:'14rem', borderColor:'#f9e401', borderWidth:'4px'}}>
                <Card.Body>
                  <Card.Title style={{color: '#121B4F'}}>3. Revisa</Card.Title>
                  <Card.Text mb-3 style={{color: '#47525E'}}>
                    El apartado de grabaciones para encontrar todas las llamadas que se generan para conocer mejor a tus clientes. 
                  </Card.Text>
                </Card.Body>
              </Card>
              <br />
        </div>
        <div class='col-auto'>  
        <Card style={{ width: '15rem', height:'14rem', borderColor:'#f9e401', borderWidth:'4px'}}>
          <Card.Body>
            <Card.Title style={{color: '#121B4F'}}>4. Ejecuta</Card.Title>
            <Card.Text mb-3 style={{color: '#47525E'}}>
              Con la información seleccionada el en botón de generar algoritmo para que el NLP corra con tus reglas.  
            </Card.Text>
          </Card.Body>
          </Card>
          <br />
        </div>
    </div>
 </div>
)
}

export default HomeScreen;