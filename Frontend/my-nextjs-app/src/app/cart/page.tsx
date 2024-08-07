"use client";
import React, { useState } from "react";
import NavbarPage from "../component/navbar";

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  subtotal?: number;
}

const initialProducts: Product[] = [
  {
    id: 1,
    name: "Botol Yakult",
    price: 10000,
    image: "https://via.placeholder.com/70",
  },
  {
    id: 2,
    name: "Botol Susu",
    price: 15000,
    image: "https://via.placeholder.com/70",
  },
];

export default function ShoppingCart() {
  const [products, setProducts] = useState<Product[]>(initialProducts);
  const [quantities, setQuantities] = useState<Record<number, number>>(
    initialProducts.reduce((acc, product) => {
      acc[product.id] = 1;
      return acc;
    }, {} as Record<number, number>)
  );
  const [shippingMethod, setShippingMethod] = useState<string>("");

  const increaseQuantity = (id: number) => {
    setQuantities((prev) => ({ ...prev, [id]: prev[id] + 1 }));
  };

  const decreaseQuantity = (id: number) => {
    setQuantities((prev) => ({
      ...prev,
      [id]: prev[id] > 1 ? prev[id] - 1 : 1,
    }));
  };

  const handleQuantityChange = (id: number, e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value);
    if (!isNaN(value) && value > 0) {
      setQuantities((prev) => ({ ...prev, [id]: value }));
    }
  };

  const calculateSubtotal = (price: number, quantity: number) => {
    return price * quantity;
  };

  const handleShippingChange = (method: string) => {
    setShippingMethod(method);
  };

  const removeProduct = (id: number) => {
    setProducts((prev) => prev.filter((product) => product.id !== id));
    setQuantities((prev) => {
      const newQuantities = { ...prev };
      delete newQuantities[id];
      return newQuantities;
    });
  };

  const totalSubtotal = products.reduce(
    (acc, product) => acc + calculateSubtotal(product.price, quantities[product.id]),
    0
  );

  return (
    <>
      <style jsx>{`
        .no-spinner::-webkit-outer-spin-button,
        .no-spinner::-webkit-inner-spin-button {
          -webkit-appearance: none;
          margin: 0;
        }

        .no-spinner {
          -moz-appearance: textfield;
        }
      `}</style>
      <div>
        <NavbarPage />
        <div className="grid pt-[45vh]">
          <h1 className="flex justify-center text-4xl">SHOPPING CART</h1>
          <div className="grid grid-cols-1 gap-10 lg:grid-cols-2 p-10">
            {/* Product Details */}
            <div className="py-10">
              <table className="w-full border-collapse">
                <thead>
                  <tr>
                    <th className="text-left">PRODUCT</th>
                    <th className="text-left">PRICE</th>
                    <th className="text-left">QUANTITY</th>
                    <th className="text-left">SUBTOTAL</th>
                    <th className="text-left">ACTION</th>
                  </tr>
                </thead>
                <tbody>
                  {products.map((product) => (
                    <tr key={product.id}>
                      <td className="py-2">
                        <div className="flex items-center">
                          <img
                            src={product.image}
                            alt={product.name}
                            className="w-16 h-16"
                          />
                          <span className="ml-4">{product.name}</span>
                        </div>
                      </td>
                      <td className="py-2">
                        RP.{product.price.toLocaleString("id-ID")}
                      </td>
                      <td className="py-2">
                        <div className="flex items-center">
                          <button
                            className="px-2 py-1 bg-gray-300 text-black w-8 h-8 flex items-center justify-center"
                            onClick={() => decreaseQuantity(product.id)}
                          >
                            -
                          </button>
                          <input
                            type="number"
                            className="px-2 py-1 border w-16 h-8 text-center no-spinner"
                            value={quantities[product.id]}
                            onChange={(e) => handleQuantityChange(product.id, e)}
                            min="1"
                            step="1"
                            onKeyDown={(e) => e.preventDefault()}
                          />
                          <button
                            className="px-2 py-1 bg-gray-300 text-black w-8 h-8 flex items-center justify-center"
                            onClick={() => increaseQuantity(product.id)}
                          >
                            +
                          </button>
                        </div>
                      </td>
                      <td className="py-2">
                        RP.{calculateSubtotal(product.price, quantities[product.id]).toLocaleString("id-ID")}
                      </td>
                      <td className="py-2">
                        <button
                          onClick={() => removeProduct(product.id)}
                          className="text-red-500"
                        >
                          <i className="fa fa-close"></i>
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Cart Totals */}
            <div className="py-10">
              <p className="text-lg font-semibold">CART TOTALS</p>
              <table className="w-full border-collapse">
                <tbody>
                  <tr>
                    <td className="py-2 text-left">SUBTOTAL</td>
                    <td className="py-2 text-right">
                      RP.{totalSubtotal.toLocaleString("id-ID")}
                    </td>
                  </tr>
                </tbody>
              </table>
              <form action="/action_page.php" className="mt-4">
                <div className="mb-4">
                  <input
                    type="text"
                    placeholder="Email@example.com"
                    className="border border-gray-300 rounded w-full"
                  />
                </div>
                <div className="flex gap-2 mb-4">
                  <div>
                    <input
                      type="checkbox"
                      id="freeShipping"
                      name="freeShipping"
                      checked={shippingMethod === "freeShipping"}
                      onChange={() => handleShippingChange("freeShipping")}
                    />
                    <label htmlFor="freeShipping"> Free Shipping</label>
                  </div>
                  <div>
                    <input
                      type="checkbox"
                      id="localPickup"
                      name="localPickup"
                      checked={shippingMethod === "localPickup"}
                      onChange={() => handleShippingChange("localPickup")}
                    />
                    <label htmlFor="localPickup"> Local Pickup</label>
                  </div>
                </div>
                <div className="grid gap-2 mb-4">
                  <label htmlFor="coupon">Coupon</label>
                  <input
                    type="text"
                    name="coupon"
                    className="border border-gray-300 rounded w-full"
                  />
                  <button className="px-2 py-2 bg-gray-500 text-black rounded w-full">
                    Apply coupon
                  </button>
                </div>
                <div className="mb-4">
                  <p>PAYMENT METHOD</p>
                  <div className="flex gap-2">
                    {["TRANSFER", "COD", "PAYLATER", "PDCPAY"].map((payment) => (
                      <button
                        key={payment}
                        type="button"
                        className="flex border p-2 text-white bg-custom-green hover:bg-custom-green/80 text-xs"
                      >
                        {payment}
                      </button>
                    ))}
                  </div>
                </div>
                <div>
                  <input
                    type="submit"
                    value="PROCESS TO CHECKOUT"
                    className="px-2 py-2 bg-blue-500 text-white rounded w-full"
                  />
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
