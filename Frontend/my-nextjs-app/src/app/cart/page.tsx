'use client';
import React, { useState } from "react";
import NavbarPage from "../component/navbar";

export default function ShoppingCart(){
  const [quantity, setQuantity] = useState(1); // State untuk kuantitas produk

  
  const increaseQuantity = () => {
    setQuantity((prev) => prev + 1);
  };

  const decreaseQuantity = () => {
    setQuantity((prev) => (prev > 1 ? prev - 1 : 1)); // Jangan biarkan kuantitas kurang dari 1
  };
  return (
    <>
    <div>
    <div><NavbarPage/></div>
    <div className="grid pt-[45vh] p-10">
      <h1 className="flex justify-center text-4xl">SHOPPING CART</h1>
      <div className="flex justify-between">
      <p>PRODUCT</p>
      <div className="flex gap-10">
      <p>PRICE</p>
     <p>QUANTITY</p>
     <p>SUBTOTAL</p>
      </div>
      </div>
      <div className="flex justify-between">
      <div className="flex gap-10">
      <img src="https://via.placeholder.com/70"/>
      <p className="mb-4 max-w-md">
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. A, quae? Laudantium est</p>
      </div>
      <div className="flex gap-10">
        <p>RP.10.000</p>
        <div>
        <button
        className="px-2 py-1 bg-gray-300 text-black mr-1"
        onClick={decreaseQuantity}
      >
        -
      </button>
      <span className="px-2 py-1 border">{quantity}</span>
      <button
        className="px-2 py-1 bg-gray-300 text-black ml-1"
        onClick={increaseQuantity}
      >
        +
      </button>
        </div>
        <p></p>
      </div>
      </div>
    </div>
    </div>
    </>
  )
}