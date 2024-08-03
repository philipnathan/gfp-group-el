// src/app/product/page.tsx
"use client";

import React, { useEffect, useState } from "react";
import NavbarPage from "../component/navbar";
import FooterDash from "../component/footer";

interface Product {
  image_url: string;
  is_active: number;
  name: string;
  price: number;
}

export default function ProductPage() {
  const [allProducts, setAllProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchAllProducts() {
      try {
        const res = await fetch('http://127.0.0.1:5000/api/products/user');
        console.log(res)
        if (!res.ok) {
          throw new Error('Failed to fetch All Products');
        }
        const data = await res.json();
        setAllProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
        setError('Error loading products');
      } finally {
        setLoading(false);
      }
    }
    fetchAllProducts();
  }, []);

  if (loading) {
    return <main>Loading...</main>;
  }

  if (error) {
    return <main>{error}</main>;
  }

  return (
    <>
      <NavbarPage />
      <div className="grid pt-[25vh] md:pt-[38vh] lg:pt-[35vh]">
        <div className="p-6">
          <div className="grid grid-cols-3 md:grid-cols-6 lg:grid-cols-9 gap-6">
            {allProducts.map((product) => (
              <div key={product.name} className="bg-white shadow-md rounded-lg overflow-hidden transition-transform duration-500 hover:scale-105">
                <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover" />
                <div className="p-4">
                  <h2 className="text-lg font-bold mb-2">{product.name}</h2>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <FooterDash />
    </>
  );
}