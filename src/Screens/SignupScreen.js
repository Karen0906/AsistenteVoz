import React from 'react';

function SignupScreen() {
  console.log('signUp')
  
  return (
    <>
      <div className="card m-5 justify-center" style={{width: '450px'}}>
        <div className="text-center fs-1 mt-2 " style={{color: 'red-100'}}>
          <strong>Registrarse</strong>
        </div>
        <div className="card-body">
          <div className="text-center m-2 mb-5 fs-4">
            Crea tu cuenta usando el nombre y correo que usas en tu empresa 
          </div>
          <form>
          <div className="mb-3" >
            <input type="name" placeholder='Nombre' className="form-control" id="name" aria-describedby="CompanyName" style={{height: '60px'}}/>
          </div>
          <div className="mb-3">
            <input type="email" placeholder='Correo' className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" style={{height: '60px'}}/>
          </div>
          <div className="mb-3">
            <input type="password" className="form-control" id="exampleInputPassword1" placeholder='Contraseña' style={{height: '60px'}}/>
          </div>
        </form>
        </div>
        <div className={`text-muted text-center mb-3`}>
          <button type="submit" className={`btn text-white`} style={{width: '250px', backgroundColor: '#c20076'}}>Aceptar</button>
        </div>
      </div>
    </>
  )
}

export default SignupScreen;