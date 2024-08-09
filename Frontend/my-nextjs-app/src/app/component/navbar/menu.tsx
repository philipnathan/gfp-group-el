'use client';
import Head from 'next/head';
import Link from 'next/link';
import React, { useState } from "react";

export default function MenuNav() {
  const [selectedOptions, setSelectedOptions] = useState({
    Fashion: "",
    Jewellery: "",
    Footwear: "",
    Home: "",
    home: "",
    gift: ""
  });

  const handleChange = (event: React.ChangeEvent<HTMLSelectElement>, category: string) => {
    const selectedValue = event.target.value;
    setSelectedOptions(prevState => ({
      ...prevState,
      [category]: selectedValue
    }));

    if (selectedValue) {
      window.location.href = selectedValue;
    }
  };

  return (
    <>
      <Head>
        <title>Menu Section</title>
      </Head>
      <div className='text-custom-Olive-Drab'>
        <Link href="/" className="p-2 border border-gray-300 rounded">
          Home
        </Link>
        <select
          value={selectedOptions.Fashion}
          onChange={(e) => handleChange(e, 'Fashion')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Fashion</option>
          <option value="/Dress">Dress</option>
          <option value="/Top">Top</option>
          <option value="/toys">T-shirt</option>
          <option value="/toys">Pants</option>
          <option value="/toys">Coat</option>
          <option value="/toys">Skirts</option>
          <option value="/toys">Jackets</option>
        </select>
        <select
          value={selectedOptions.Jewellery}
          onChange={(e) => handleChange(e, 'Jewellery')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="/">Jewellery</option>
          <option value="/earing">Earing</option>
          <option value="/neckless">Neckless</option>
          <option value="/rings">rings</option>
        </select>
        <select
          value={selectedOptions.Footwear}
          onChange={(e) => handleChange(e, 'Footwear')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Footwear</option>
          <option value="/shoes">Shoes</option>
          <option value="/sandals">Sandals</option>
          <option value="/sneaker">Sneakers</option>
          <option value="/boots">boots</option>
        </select>
        <select
          value={selectedOptions.Home}
          onChange={(e) => handleChange(e, 'Home')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Home</option>
          <option value="/furnitur">Furniture</option>
          <option value="/mens-shoes">Decor</option>
        </select>
        <select
          value={selectedOptions.home}
          onChange={(e) => handleChange(e, 'home')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Home & Living</option>
          <option value="/home-decor">Home Decor</option>
        </select>
        <select
          value={selectedOptions.gift}
          onChange={(e) => handleChange(e, 'gift')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Gifts & Collectibles</option>
          <option value="/gifts">Gifts</option>
        </select>
        <Link href="/about-us" className="p-2 border border-gray-300 rounded">
          About Us
        </Link>
      </div>
    </>
  );
}
