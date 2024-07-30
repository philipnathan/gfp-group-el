'use client';
import React, { FormEvent } from "react";

export default function SearchNav() {
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const searchValue = (e.target as HTMLFormElement).search.value;
    console.log("Searching for:", searchValue);
  };

  return (
    <div className="p-10">
      <form onSubmit={handleSubmit} className="flex items-center">
        <input
          type="text"
          placeholder="Search"
          name="search"
          className="search-input p-2 border border-gray-300 rounded"
        />
        <button type="submit" className="search-button ml-2 bg-custom-green text-white px-4 py-2 rounded">
        <i className="fa fa-search"></i>
        </button>
      </form>
    </div>
  );
}
