'use client';
import { useState } from "react";
import NavbarPage from "../../component/navbar";
import FooterDash from "../../component/footer";

interface Product {
  id: number;
  name: string;
  image: { src: string; alt: string; bgColor: string }[];
  Description: string;
}

const product: Product = {
  id: 1,
  name: "Botol Yakult",
  Description: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. A, quae? Laudantium est",
  image: [
    { src: "https://via.placeholder.com/400", alt: "PRODUCT 1", bgColor: "bg-green-500" },
    { src: "https://via.placeholder.com/400", alt: "PRODUCT 2", bgColor: "bg-yellow-500" },
    { src: "https://via.placeholder.com/400", alt: "PRODUCT 3", bgColor: "bg-red-500" },
  ]
};

export default function DetailProduct() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [quantity, setQuantity] = useState(1);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev === product.image.length - 1 ? 0 : prev + 1));
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev === 0 ? product.image.length - 1 : prev - 1));
  };

  const increaseQuantity = () => {
    setQuantity((prev) => prev + 1);
  };

  const decreaseQuantity = () => {
    setQuantity((prev) => (prev > 1 ? prev - 1 : 1));
  };

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <NavbarPage />
      <div className="pt-[25vh] md:pt-[38vh] lg:pt-[35vh]">
        <div className="grid grid-cols-1 gap-10 lg:grid-cols-2 justify-center gap-10 p-10">
          <div className="relative">
            <div className={`flex justify-center overflow-hidden p-10 ${product.image[currentSlide].bgColor}`} onClick={openModal}>
              <img
                src={product.image[currentSlide].src}
                alt={product.image[currentSlide].alt}
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
            <h1 className="text-3xl mb-4 font-bold">{product.name}</h1>
            <p className="mb-4 max-w-md"></p>
            <div className="pt-4 max-w-md">
              <p>{product.Description}</p>
            </div>
            <p className="mb-4">In Stock</p>
            <div className="flex items-center mb-4">
              <button
                className="px-4 py-2 bg-gray-300 text-black mr-2"
                onClick={decreaseQuantity}
              >
                -
              </button>
              <span className="px-4 py-2 border">{quantity}</span>
              <button
                className="px-4 py-2 bg-gray-300 text-black ml-2"
                onClick={increaseQuantity}
              >
                +
              </button>
            </div>
            <div>
              <button className="px-6 bg-blue-500 text-white rounded">Add to Cart</button>
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
              &times;
            </button>
            <img
              src={product.image[currentSlide].src}
              alt={product.image[currentSlide].alt}
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
