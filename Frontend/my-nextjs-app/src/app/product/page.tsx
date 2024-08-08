'use client'
import React, { useEffect, useState } from "react";
import Link from 'next/link'; 
import NavbarPage from "../component/navbar";
import FooterDash from "../component/footer";

interface Product {
  id: number;
  image_url: string;
  is_active: number;
  name: string;
  price: number;
  seller_id: number
}
interface Location {
  id: number;
  district: string;
  province_id: number;
}


export default function ProductPage() {
  const [allProducts, setAllProducts] = useState<Product[]>([]);
  const [allLocations, setAllLocations] = useState<Location[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    async function fetchAllProducts() {
      try {

        const locationRes = await fetch('http://127.0.0.1:5000/api/locations/districts');
        if (!locationRes.ok) {
          throw new Error('Failed to fetch locations');
        }
        const locationsData = await locationRes.json();
        setAllLocations(locationsData);

        const res = await fetch('http://127.0.0.1:5000/api/products/user');
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
    return (
      <main className="flex items-center justify-center min-h-screen">
        <div className="flex items-center">
          <svg
            className="animate-spin h-8 w-8 text-blue-500"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
              fill="none"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v3a5 5 0 00-5 5h3a2 2 0 01-2 2v3z"
            />
          </svg>
          <span className="ml-3 text-lg text-gray-700">Loading...</span>
        </div>
      </main>
    );
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
            <Link href={`/product/detail-product?id=${product.id}`} key={product.id}>
            <div className="bg-white shadow-md rounded-lg overflow-hidden transition-transform duration-500 hover:scale-105">
              <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover" />
              <div className="p-4">
                <h2 className="text-lg font-bold mb-2">{product.name}</h2>
                <p>Rp.{product.price}</p>
                {allLocations.map((loc)=>(
                  <p>{loc.district}</p>
                ))}
              </div>
            </div>
          </Link>
          
            ))}
          </div>
        </div>
      </div>
      <FooterDash />
    </>
  );
}
