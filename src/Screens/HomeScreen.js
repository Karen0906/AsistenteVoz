import React from 'react';
import Card from 'react-bootstrap/Card';

function HomeScreen() {

  return (
    <div class='container'>
      <div class='hero-unit'>
        <h1 class= 'mt-5'> Conmutador a asistentes de voz</h1>
        <p>El nuevo sistema de conmutación automatizado que sea capaz de conectarse a varios motores conversacionales y seleccionar el mejor de acuerdo a la entrada del usuario</p>
        <p>
        </p>
      </div>
      <div class='row gx-1'>
        <div class='col-auto'>
          <Card border='warning' style={{ width: '15rem', height:'12rem'}} className='border border-4'>
                <Card.Body>
                  <Card.Title>1. Selecciona</Card.Title>
                  <Card.Text mb-3>
                    Las preguntas que más se relacionen a tu negocio, importa documentos csv, añade y edita lo que necesites. 
                  </Card.Text>
                </Card.Body>
              </Card>
              <br />
        </div>
        <div class='col-auto'>
            <Card border='warning' style={{ width: '15rem', height:'12rem' }} className='border border-4'>
                  <Card.Body>
                    <Card.Title >2. Aporta</Card.Title>
                    <Card.Text mb-3>
                      Los documentos, respuestas o información relevante relacionada a las preguntas previamente elegidas.
                    </Card.Text>
                  </Card.Body>
                </Card>
                <br />
        </div>
  {/* <div class='w-100'></div> */}
        <div class='col-auto'>
          <Card border='warning' style={{ width: '15rem', height:'12rem' }} className='border border-4'>
                <Card.Body>
                  <Card.Title>3. Revisa</Card.Title>
                  <Card.Text mb-3>
                    El apartado de grabaciones para encontrar todas las llamadas que se generan para conocer mejor a tus clientes. 
                  </Card.Text>
                </Card.Body>
              </Card>
              <br />
        </div>
        <div class='col-auto'>  <Card border='warning' style={{ width: '15rem', height:'12rem' }} className='border border-4'>
          <Card.Body>
            <Card.Title>4. Ejecuta</Card.Title>
            <Card.Text mb-3>
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