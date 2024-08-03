'use client'
import { useState } from "react";
import NavbarPage from "../component/navbar";
import FooterDash from "../component/footer";


export default function DetailProduct() {
  const images = [
    { id: 1, src: "https://via.placeholder.com/400", alt: "PRODUCT 1", bgColor: "bg-green-500" },
    { id: 2, src: "https://via.placeholder.com/400", alt: "PRODUCT 2", bgColor: "bg-yellow-500" },
    { id: 3, src: "https://via.placeholder.com/400", alt: "PRODUCT 3", bgColor: "bg-red-500" },
    { id: 4, src: "https://via.placeholder.com/400", alt: "PRODUCT 4", bgColor: "bg-blue-500" },
    { id: 5, src: "https://via.placeholder.com/400", alt: "PRODUCT 5", bgColor: "bg-gray-500" },
    { id: 6, src: "https://via.placeholder.com/400", alt: "PRODUCT 6", bgColor: "bg-purple-500" }
  ];

  const [currentSlide, setCurrentSlide] = useState(0);
  const [quantity, setQuantity] = useState(1); // State untuk kuantitas produk

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev === images.length - 1 ? 0 : prev + 1));
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev === 0 ? images.length - 1 : prev - 1));
  };

  const increaseQuantity = () => {
    setQuantity((prev) => prev + 1);
  };

  const decreaseQuantity = () => {
    setQuantity((prev) => (prev > 1 ? prev - 1 : 1)); // Jangan biarkan kuantitas kurang dari 1
  };

  return (
    <>
    <NavbarPage/>
    <div className="pt-[45vh]">
      <div className="flex justify-center gap-10">
        <div className="relative">
          <div className={`flex justify-center overflow-hidden p-10 ${images[currentSlide].bgColor}`}>
            <img
              src={images[currentSlide].src}
              alt={images[currentSlide].alt}
              className="object-cover"
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
          <h1 className="text-3xl mb-4 font-bold">Nama Productnya apa</h1>
          <p className="mb-4 max-w-md">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. A, quae? Laudantium est</p>
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
          <div className="pt-4 max-w-md">
          <p>Deskripsi: Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quia officia hic atque tenetur, nemo ipsam, laborum accusantium deserunt non sapiente, voluptatibus iusto veritatis laudantium est voluptatem magni perspiciatis corrupti at.
          </p>
          </div>
        </div>
      </div>
    </div>
    <FooterDash/>
    </>
  );
}