// "use client";

// import Forms from "../components/Form/Forms";

// const Login = () => {
//   const loginIntialValue = {};
//   const loginFields = [
//     {
//       textLabel: "Email",
//       fieldName: "email",
//       fieldPlaceholder: "Enter your email address",
//       errorComponent: "div",
//     },
//     {
//       textLabel: "Password",
//       fieldName: "password",
//       fieldPlaceholder: "Enter your password",
//       errorComponent: "div",
//     },
//   ];
//   function onSubmit(values: any) {
//     handleLogin(values);
//     setTimeout(() => {
//       navigate("/home");
//     }, 5000);
//   }
//   return (
//     <Flex
//       direction="column"
//       className="w-screen h-screen justify-center items-center bg-gradient-to-b from-red-400 to-red-200 overflow-auto"
//     >
//       <Navbar />

//       <Forms
//         fields={loginFields}
//         onSubmit={onSubmit}
//         initValues={loginIntialValue}
//         btnName="Login"
//       />
//     </Flex>
//   );
// };

// export default Login;
