import React from "react"
import NavbarPage from "../component/navbar"
import FooterDash from "../component/footer"


export default function product(){
    return(
        <>
        <NavbarPage/>
        <div className="grid pt-[25vh] md:pt-[38vh] lg:pt-[35vh]">
      <div className="p-6">
        <div className="grid grid-cols-3 md:grid-cols-6 lg:grid-cols-9 gap-6">
          {[
            "BOTOL YAKULT",
            "POPMIE",
            "LARUTAN PENYEGAR",
            "SUNLIGHT CUCI PIRING",
            "BERAS CAP LELE",
            "LOTION CITRA",
            "PARFUM CHANNEL",
            "AQUA 300ML",
            "PIZZA HUT",
            "TUPPERWARE BOX",
            "HAT BUCKET ZARA",
            "FLOWER PALSU",
            "YAKULT 12ML",
            "POPMIE KARI",
            "LARUTAN CAP BADAK",
            "CUCI PIRING SUNLIGHT",
            "BERAS ROJO LELE",
            "LOTION MARINA",
            "PARFUM ZARA",
            "AQUA 200ML",
            "DOMINO PIZZA",
            "TUPPERWARE CUP",
            "HAT BUCKET LV",
            "FLOWER ASLI",
            "BOTOL YAKULT 2ML",
            "POPMIE SOTO",
            "LARUTAN KAKI TIGA",
            "CUCI PIRING MAMA LEMON",
            "BERAS MERAH",
            "LOTION ANTI NYAMUK",
            "PARFUM EAU DE PARFUM",
            "AQUA GELAS",
            "PIZZA DOMINO",
            "TUPPERWARE GLASS",
            "HAT BUCKET",
            "ROSE FLOWER",
          ].map((item, index) => (
            <div key={index} className="bg-white shadow-md rounded-lg overflow-hidden transition-transform duration-500 hover:scale-105">
              <img src="https://via.placeholder.com/200" alt={item} className="w-full h-48 object-cover" />
              <div className="p-4">
                <h2 className="text-lg font-bold mb-2">{item}</h2>
              </div>
            </div>
          ))}
        </div>
      </div>
      </div>
      <FooterDash/>
        </>
    )
}