import { useState } from 'react';
import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card";
import { useRouter } from 'next/navigation';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  quantity?: number;
}

const initialProducts: Product[] = [
  {
    id: 1,
    name: "Botol Yakult",
    price: 10000,
    image: "https://via.placeholder.com/30",
    quantity: 1,
  },
  {
    id: 2,
    name: "Botol Susu",
    price: 15000,
    image: "https://via.placeholder.com/30",
    quantity: 1,
  },
];

interface NavCartProps {
  onSeeAllClick: () => void;
}

export default function NavCart({ onSeeAllClick }: NavCartProps) {
  const [products, setProducts] = useState<Product[]>(initialProducts);
  const router = useRouter();

  const handleNavCartClick = () => {
    router.push('/cart');
  };

  return (
    <HoverCard>
      <HoverCardTrigger>
        <button 
          className="w-full bg-custom-green text-white p-2 rounded hover:bg-custom-green/80 transition duration-300"
          onClick={handleNavCartClick}
        >
          <i className="fa fa-shopping-cart"></i>
        </button>
      </HoverCardTrigger>
      <HoverCardContent className="max-w-lg">
        <div className="p-4">
          <table className="w-full text-sm">
            <tbody>
              {products.map((product) => (
                <tr key={product.id}>
                  <td className="py-1">
                    <div className="flex items-center">
                      <img
                        src={product.image}
                        alt={product.name}
                        className="w-10 h-10"
                      />
                      <span className="ml-2">{product.name}</span>
                    </div>
                  </td>
                  <td className="py-2 text-center">
                    {product.quantity}
                  </td>
                  <td className="py-2">
                    Rp.{product.price.toLocaleString("id-ID")}
                  </td>
                  <td className="py-2 text-center">
                    x {product.quantity}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="mt-4 flex justify-end">
            <button 
              onClick={onSeeAllClick}
              className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition duration-300"
            >
              See All
            </button>
          </div>
        </div>
      </HoverCardContent>
    </HoverCard>
  );
}
