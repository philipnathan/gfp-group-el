'use client';

import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import NavbarPage from '../../component/navbar';
import FooterDash from '../../component/footer';

interface Review {
  rating: number;
  review: string;
}

interface Product {
  avg_rating: number;
  description: string;
  image_url: string[];
  name: string;
  price: number;
  reviews: Review[];
  sold_qty: number;
  stock: number;
  volume_m3: number;
  weight_kg: number;
}

export default function DetailProductPage() {
  const searchParams = useSearchParams();
  const id = searchParams.get('id');
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [quantity, setQuantity] = useState(1);
  const [quantityError, setQuantityError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [singleImageMessage, setSingleImageMessage] = useState<string | null>(null);
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    if (id) {
      const fetchProduct = async () => {
        try {
          const res = await fetch(`http://127.0.0.1:5000/api/products/user/product/${id}`);
          if (!res.ok) throw new Error('Failed to fetch product');
          const data = await res.json();
          setProduct(data);
        } catch (error) {
          console.error('Error fetching product:', error);
          setError('Error loading product');
        } finally {
          setLoading(false);
        }
      };
      fetchProduct();
    }
  }, [id]);

  const nextSlide = () => {
    if (!product) return;
    const numberOfImages = product.image_url.length;
    if (numberOfImages <= 1) {
      setSingleImageMessage('There is only one picture');
      return;
    }
    setCurrentSlide((prev) => (prev === numberOfImages - 1 ? 0 : prev + 1));
    setSingleImageMessage(null);
  };

  const prevSlide = () => {
    if (!product) return;
    const numberOfImages = product.image_url.length;
    if (numberOfImages <= 1) {
      setSingleImageMessage('There is only one picture');
      return;
    }
    setCurrentSlide((prev) => (prev === 0 ? numberOfImages - 1 : prev - 1));
    setSingleImageMessage(null);
  };

  const increaseQuantity = () => {
    if (product) {
      setQuantity((prev) => {
        const newQuantity = prev + 1;
        if (newQuantity > product.stock) {
          setQuantityError(`Maximum quantity to purchase this item is ${product.stock}`);
          return prev;
        }
        setQuantityError(null);
        return newQuantity;
      });
    }
  };

  const decreaseQuantity = () => {
    setQuantity((prev) => {
      const newQuantity = prev > 1 ? prev - 1 : 1;
      setQuantityError(null);
      return newQuantity;
    });
  };

  const openModal = () => setIsModalOpen(true);

  const closeModal = () => setIsModalOpen(false);

  const handleQuantityChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    if (value === '') {
      setQuantity(1);
      setQuantityError(null);
      return;
    }
    const numberValue = parseInt(value, 10);
    if (!isNaN(numberValue) && numberValue > 0) {
      if (product && numberValue > product.stock) {
        setQuantityError(`Maximum quantity to purchase this item is ${product.stock}`);
        setQuantity(product.stock);
      } else {
        setQuantityError(null);
        setQuantity(numberValue);
      }
    } else {
      setQuantityError('Please enter a valid number');
    }
  };

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
      <style jsx>{`
        .no-spinner::-webkit-outer-spin-button,
        .no-spinner::-webkit-inner-spin-button {
          -webkit-appearance: none;
          margin: 0;
        }

        .no-spinner {
          -moz-appearance: textfield;
        }

        table {
          border-collapse: collapse;
          width: 100%;
        }

        th, td {
          border: 1px solid #ddd;
          padding: 8px;
        }

        th {
          text-align: left;
          font-weight: bold;
        }

        td {
          font-weight: normal;
        }
      `}</style>
      <NavbarPage />
      <div className="pt-[25vh] md:pt-[38vh] lg:pt-[35vh]">
        <div className="grid grid-cols-1 gap-10 lg:grid-cols-2 justify-center p-10">
          <div className="relative">
            <div className="flex justify-center overflow-hidden p-10" onClick={openModal}>
              <img
                src={product?.image_url[currentSlide]}
                alt={`Product Image ${currentSlide + 1}`}
                className="object-cover cursor-pointer"
                style={{ width: '400px', height: '400px' }}
              />
            </div>
            <a
              className="absolute left-0 top-1/2 transform -translate-y-1/2 px-3 py-2 bg-black text-white cursor-pointer z-10"
              onClick={prevSlide}
            >
              &#10094;
            </a>
            <a
              className="absolute right-0 top-1/2 transform -translate-y-1/2 px-3 py-2 bg-black text-white cursor-pointer z-10"
              onClick={nextSlide}
            >
              &#10095;
            </a>
          </div>
          <div className="flex flex-col font-sans">
            <h1 className="text-3xl mb-4 font-bold">{product?.name}</h1>
            <p className="mb-4">In Stock: {product?.stock}</p>
            <p className="mb-4">Rp.{product?.price}</p>
            <div className="flex items-center mb-4">
              <button
                className="px-4 py-2 bg-gray-300 text-black mr-2"
                onClick={decreaseQuantity}
              >
                -
              </button>
              <input
                type="number"
                className="px-4 py-2 border text-center w-16 h-10 no-spinner"
                value={quantity}
                onChange={handleQuantityChange}
                min="1"
              />
              <button
                className="px-4 py-2 bg-gray-300 text-black ml-2"
                onClick={increaseQuantity}
              >
                +
              </button>
            </div>
            {quantityError && (
              <p className="text-red-500 mb-4">{quantityError}</p>
            )}
            <div>
              <button className="px-6 bg-blue-500 text-white rounded">Add to Cart</button>
            </div>
            <div className="pt-4 max-w-md">
              <p>{product?.description}</p>
            </div>
            <div className="pt-4">
              <table>
                <thead>
                  <tr>
                    <th>Sold</th>
                    <th>Volume</th>
                    <th>Weight</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>{product?.sold_qty} pcs</td>
                    <td>{product?.volume_m3} m³</td>
                    <td>{product?.weight_kg} kg</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div className="pt-4 max-w-md">
              <p><strong>Description:</strong> {product?.description}</p>
            </div>
            <div className="pt-4 max-w-md">
              <h2 className="text-xl font-bold mb-2">Reviews</h2>
              {product?.reviews.length === 0 ? (
                <p>No reviews yet</p>
              ) : (
                product?.reviews.map((review, index) => (
                  <div key={index} className="border-b-2 border-gray-200 py-2">
                    <p><strong>Rating:</strong> {review.rating}</p>
                    <p><strong>Review:</strong> {review.review}</p>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
        </div>
        {isModalOpen && (
          <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50">
            <div className="relative p-4 bg-white rounded">
            <button
                className="absolute top-2 right-2 text-xl font-bold"
                onClick={closeModal}
              >
                X
              </button>
              <img
                src={product?.image_url[currentSlide]}
                alt={`Product Image ${currentSlide}`}
                className="object-cover"
                style={{ maxWidth: '90vw', maxHeight: '80vh' }}
              />
            
            </div>
          </div>
        )}
      
      <FooterDash />
    </>
  );
}
