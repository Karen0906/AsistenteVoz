import React, {useState} from 'react';
import '../Screens/ProfileStyles.css';

function Profile() {

  const[predeterminado, setPredeterminado] = useState(true);
  const[clasificador, setClasificador] = useState(true);
  const[temas, setTemas] = useState(1);

  var temasNombres = [];
  for (var i = 0; i < parseInt(temas); i++) {
    temasNombres.push(i);
  }


	return (
    <div className='Wrapper'>
      <div className='Container'>
        <h1 className='fw-bold display-4' style={{color:'#121B4F'}}>Amazon</h1>
        <form>
          <h4 className='fw-bold pt-3' style={{color:'#121B4F'}}>1. Personalice el modelo para su NLP</h4>
          <p className='mb-0' style={{color:'#47525E'}}>Ingrese la información que se solicita en los siguientes pasos para que coincida con sus reglas de negocio.</p>
          <h5 className='fw-bold pt-3'style={{color:'#121B4F'}}>1.1 Seleccione el modelo para pre-entrenar</h5>
          <p className='mb-0' style={{color:'#47525E'}}>Utilice nuestro modelo o ingrese el enlace a alguno de su preferencia.</p>
          <div className='form-check form-switch mt-0'>
            <input className='form-check-input' type='checkbox' id='modeloSwitch' onClick={()=>setPredeterminado(!predeterminado)} defaultChecked/>
            {predeterminado ? <label style={{color:'#47525E'}} className='form-check-label ' for='modeloSwitch'>Predeterminado (referenciar)</label> : <p className='mx-0 my-0'></p>}
          </div>
          {predeterminado ? <p className='mx-0 my-0'></p> : <input type='text' class='form-control' id='linkModel' placeholder='https://mimodelo.com'/>}
          <h5 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.2 Seleccione el tipo de clasificador del NLP</h5>
          <p className='mb-1' style={{color:'#47525E'}}>Esta decisión dependerá de la información con la que cuente su empresa para el modelo.</p>
          <div className='d-flex flex-row justify-content-around align-items-center'>
            <div className='btn-group' role='group'>
              <input type='radio' className='btn-check' name='clasificador' id='clasificador1' autocomplete='off' onClick={()=>setClasificador(true)} defaultChecked/>
              <label className='btn btn-outline-primary' for='clasificador1'>
                <div className='d-flex align-items-center justify-content-center flex-column px-2 py-2 '>
                  <p className='mt-0 mb-0 fw-bold'>Automático</p>
                  <p className='mt-0 mb-0'>Ingrese las respuestas y el clasificador las ordenará por contextos.</p>
                </div>
              </label>
              <input type='radio' className='btn-check' name='clasificador' id='clasificador2' autocomplete='off' onClick={()=>setClasificador(false)}/>
              <label className='btn btn-outline-primary' for='clasificador2'>
                <div className='d-flex align-items-center justify-content-center flex-column px-2 py-2'>
                  <p className='mt-0 mb-0 fw-bold'>Manual</p>
                  <p className='mt-0 mb-0'>Ingrese los contextos y respuestas relacionadas por cada uno. </p>
                </div>
              </label>
            </div>
          </div>
          {clasificador ?
          <div className='d-flex flex-column'>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.2.1 Añada las respuestas para el modelo</h6>
            <label for="formFile" class="form-label" style={{color:'#47525E'}}>Importe un archivo tipo csv con toda la información que satisfaga las preguntas de sus clientes.</label>
            <input class="form-control" type="file" id="formFile"/>
            <h5 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3 Variables del modelo</h5>
            <p className='mb-0' style={{color:'#47525E'}}>Personalice los valores de tu modelo para que se acomoden a lo que más nececesita su empresa.</p>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3.1  BERT</h6>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3.2  PCA</h6>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3.3  K-means</h6>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3.4  Word to vector</h6>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3.5  Speech to text</h6>
            <div className='d-flex flex-row pt-3'>
              <button type="submit" class="btn btn-primary">Submit</button>
            </div>
            <h4 className='fw-bold pt-3' style={{color:'#121B4F'}}>2. Dashboard</h4>
            <p className='mb-0' style={{color:'#47525E'}}>Visualice si las variables del modelo se adaptan a sus necesidades.</p>
            <h4 className='fw-bold pt-3' style={{color:'#121B4F'}}>3. Llamadas realizadas</h4>
            <p className='mb-0' style={{color:'#47525E'}}>Revise el transcript de las conversaciones que ha tenido el NLP.</p>
          </div>
          :
          <div className='d-flex flex-column'>
            <h6 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.2.1 Contextos</h6>
            <p className='mb-0' style={{color:'#47525E'}}>Ingrese la cantidad de contextos/temas que quiere tener en su NLP.</p>
            <div className='d-flex flex-row justify-content-around align-items-center'>
            {temas > 1 ?
              <div className='btn-group' role='group'>
                <input type='radio' className='btn-check' name='temas' id='temas1' autocomplete='off' onClick={()=>setTemas(temas - 1)}/>
                <label className='btn btn-outline-primary' for='temas1'>-</label>
                <input type='radio' className='btn-check' name='temas' id='temas2' autocomplete='off'/>
                <label className='btn btn-outline-primary' for='temas2'>{temas}</label>
                <input type='radio' className='btn-check' name='temas' id='temas3' autocomplete='off' onClick={()=>setTemas(temas + 1)}/>
                <label className='btn btn-outline-primary' for='temas3'>+</label>
              </div>
              :
              <div className='btn-group' role='group'>
                <input type='radio' className='btn-check' name='temas' id='temas1' autocomplete='off'/>
                <label className='btn btn-outline-primary' for='temas1'>{temas}</label>
                <input type='radio' className='btn-check' name='temas' id='temas2' autocomplete='off' onClick={()=>setTemas(temas + 1)}/>
                <label className='btn btn-outline-primary' for='temas2'>+</label>
              </div>
            }
            </div>
            <div className='d-flex flex-column pt-3'>
              {temasNombres.map((t)=>(
                <div>
                  <p className='fw-bold' style={{color:'#121B4F'}}>Contexto {t+1}</p>
                  <input type='text' className='form-control mb-2' id={t+'tema'} placeholder='Tarjeta de crédito'/>
                  <label for="formFile" className="form-label mb-1" style={{color:'#47525E'}}>Importe un archivo tipo csv con toda la información que satisfaga las preguntas de sus clientes para el tema seleccionado.</label>
                  <input className="form-control mb-4" type="file" id="formFile"/>
                </div>
              ))}
            </div>
            <h5 className='fw-bold pt-3' style={{color:'#121B4F'}}>1.3 Variables del modelo</h5>
            <p className='mb-0' style={{color:'#47525E'}}>Personalice los valores de tu modelo para que se acomoden a lo que más nececesita su empresa.</p>
            <div className='d-flex flex-row pt-3'>
              <button type="submit" class="btn btn-primary">Submit</button>
            </div>
            <h4 className='fw-bold pt-3' style={{color:'#121B4F'}}>2. Dashboard</h4>
            <p className='mb-0' style={{color:'#47525E'}}>Visualice si las variables del modelo se adaptan a sus necesidades.</p>
            <h4 className='fw-bold pt-3' style={{color:'#121B4F'}}>3. Llamadas realizadas</h4>
            <p className='mb-0' style={{color:'#47525E'}}>Revise el transcript de las conversaciones que ha tenido el NLP.</p>
          </div>
          }
        </form>
      </div>
    </div>
	)
}

export default Profile;