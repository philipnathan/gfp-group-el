"use client";
import React, { useEffect, useState } from "react";

interface Location {
  id: number;
  province: string;
}

export default function FilterSearch() {
  const [locations, setLocations] = useState<Location[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(
          "http://127.0.0.1:5000/api/locations/provinces"
        );
        console.log(res);
        if (!res.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await res.json();
        setLocations(data);
      } catch (error) {
        console.error("Error fetching data:", error);
        setError("Error loading data");
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return <main>Loading...</main>;
  }

  if (error) {
    return <main>{error}</main>;
  }

  return (
    <>
      <div className="grid">
        <p className="px-10">FILTER</p>
        <label className="px-10">Location</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {locations.map((loc) => (
            <button
              key={loc.id}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {loc.province}
            </button>
          ))}
        </div>

        {/* Tipe Penjual */}
        <label className="px-10">Tipe Penjual</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {["Mall", "Star", "Star +"].map((type) => (
            <button
              key={type}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {type}
            </button>
          ))}
        </div>

        {/* Payment Method */}
        <label className="px-10">Payment Method</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {["COD", "CICILAN"].map((method) => (
            <button
              key={method}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {method}
            </button>
          ))}
        </div>

        {/* Delivery Option */}
        <label className="px-10">Delivery Option</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {[
            "INSTANT",
            "REGULER",
            "HEMAT",
            "SAMEDAY",
            "KARGO",
            "NEXT DAY",
            "INSTANT CAR",
            "AMBIL DI TEMPAT",
          ].map((option) => (
            <button
              key={option}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {option}
            </button>
          ))}
        </div>

        {/* Promo Program */}
        <label className="px-10">PROMO PROGRAM</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {[
            "CASHBACK",
            "FREE DELIVERY",
            "DISCOUNT",
            "GROSIR",
            "READY STOCK",
            "TERMURAH",
          ].map((promo) => (
            <button
              key={promo}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {promo}
            </button>
          ))}
        </div>

        {/* Price Range */}
        <label className="px-10">PRICE</label>
        <div className="px-10 flex items-center space-x-2">
          <input
            type="number"
            placeholder="MIN"
            className="border p-1 text-xs"
          />
          <input
            type="number"
            placeholder="MAX"
            className="border p-1 text-xs"
          />
        </div>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {["0-75K", "75-150K", "150-200K"].map((range) => (
            <button
              key={range}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green hover:bg-custom-pastel-green/80 text-xs"
            >
              {range}
            </button>
          ))}
        </div>
      </div>
    </>
  );
}
