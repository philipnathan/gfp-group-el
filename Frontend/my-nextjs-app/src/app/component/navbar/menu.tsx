'use client';
import Head from 'next/head';
import Link from 'next/link';
import React, { useState } from "react";

export default function MenuNav() {
  const [selectedOptions, setSelectedOptions] = useState({
    baby: "",
    fashion: "",
    jewellery: "",
    footwear: "",
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
          value={selectedOptions.baby}
          onChange={(e) => handleChange(e, 'baby')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Baby & Kids</option>
          <option value="/baby">Baby</option>
          <option value="/toys">Toys</option>
        </select>
        <select
          value={selectedOptions.fashion}
          onChange={(e) => handleChange(e, 'fashion')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Fashion</option>
          <option value="/womens-clothing">Women</option>
          <option value="/mens-clothing">Men</option>
          <option value="/accessories">Accessories</option>
        </select>
        <select
          value={selectedOptions.jewellery}
          onChange={(e) => handleChange(e, 'jewellery')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Jewellery</option>
          <option value="/earrings">Earrings</option>
          <option value="/necklaces">Necklaces</option>
        </select>
        <select
          value={selectedOptions.footwear}
          onChange={(e) => handleChange(e, 'footwear')}
          className="p-2 border border-gray-300 rounded"
        >
          <option value="">Footwear</option>
          <option value="/womens-shoes">Women</option>
          <option value="/mens-shoes">Men</option>
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
