'use client';

import React, { useEffect, useState } from "react";

interface Location {
  id: number;
  province: string;
}

interface District {
  id: number;
  district: string;
  province_id: number;
}

interface FilterSearchProps {
  onFilterChange: (filters: { locationId: number | null }) => void;
}

export default function FilterSearch({ onFilterChange }: FilterSearchProps) {
  const [locations, setLocations] = useState<Location[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedLocationId, setSelectedLocationId] = useState<number | null>(null);
  const [districts, setDistricts] = useState<District[]>([]);
  const [filteredDistricts, setFilteredDistricts] = useState<District[]>([]);
  const [activeButton, setActiveButton] = useState<number | null>(null);

  useEffect(() => {
    async function fetchLocations() {
      try {
        const res = await fetch('http://127.0.0.1:5000/api/locations/provinces');
        if (!res.ok) {
          throw new Error('Failed to fetch locations');
        }
        const data = await res.json();
        setLocations(data);
      } catch (error) {
        console.error('Error fetching locations:', error);
        setError('Error loading locations');
      } finally {
        setLoading(false);
      }
    }

    async function fetchDistricts() {
      try {
        const res = await fetch('http://127.0.0.1:5000/api/locations/districts');
        console.log(res)
        if (!res.ok) {
          throw new Error('Failed to fetch districts');
        }
        const data = await res.json();
        setDistricts(data);
      } catch (error) {
        console.error('Error fetching districts:', error);
        setError('Error loading districts');
      }
    }

    fetchLocations();
    fetchDistricts();
  }, []);

  useEffect(() => {
    if (selectedLocationId !== null) {
      const filtered = districts.filter(district => district.province_id === selectedLocationId);
      setFilteredDistricts(filtered);
      onFilterChange({ locationId: selectedLocationId });
    }
  }, [selectedLocationId, districts, onFilterChange]);

  async function handleLocationClick(locationId: number) {
    setSelectedLocationId(locationId);
    setActiveButton(locationId);
  }

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
              className={`search-button border p-1 text-xs ${activeButton === loc.id ? 'bg-custom-green text-white' : 'bg-custom-pastel-green text-custom-green'}`}
              onClick={() => handleLocationClick(loc.id)}
            >
              {loc.province}
            </button>
          ))}
        </div>

        {selectedLocationId && (
          <div className="px-10 mt-4">
            <p className="font-bold">Districts for Location ID: {selectedLocationId}</p>
            <ul className="list-disc pl-5">
              {filteredDistricts.map(district => (
                <li key={district.id}>
                  District: {district.district}, ID: {district.id}, Province ID: {district.province_id}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Tipe Penjual */}
        <label className="px-10">Tipe Penjual</label>
        <div className="px-10 grid grid-cols-3 gap-1 md:grid-cols-6 lg:grid-cols-9 lg:text-xs">
          {["Mall", "Star", "Star +"].map((type) => (
            <button
              key={type}
              type="button"
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green text-xs"
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
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green text-xs"
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
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green text-xs"
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
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green text-xs"
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
              className="search-button text-custom-green border border-custom-green p-1 bg-custom-pastel-green text-xs"
            >
              {range}
            </button>
          ))}
        </div>
      </div>
    </>
  );
}