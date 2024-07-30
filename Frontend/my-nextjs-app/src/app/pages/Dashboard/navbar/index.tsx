import React, {ReactNode} from "react";
import LOGO_PDC_RYCYCLE from '../../asset/LOGO PDC RYCYCLE.png';
import LOGO from '../../asset/LOGO.png'
import Image from "next/image";
import SearchNav from "./searchbar";
import MenuNav from "./menu";
import Head from 'next/head';
import "../../../globals.css";

import Link from 'next/link';

export default function NavbarPage(){
    return(
    <>
    <div className="grid bg-white shadow-md fixed top-0 left-0 w-full">
    <div className="flex justify-between items-center p-4 ">
        <div className="grid">
        <Image src={LOGO} alt="logo"  className="w-20 h-20" />
        <p className="text-custom-green font-bold">PDC RYCYCLE</p>
        </div>
            <Head>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
            </Head>
            <SearchNav/>
            <div className="flex items-center space-x-4">
            <button type="submit" className="search-button ml-2 bg-custom-green text-white px-4 py-2 rounded">
                login/register
            </button>
            <button type="submit" className="search-button ml-2 bg-custom-green text-white px-4 py-2 rounded">
            <i className='fa fa-shopping-cart'></i>
            </button>
        </div>
        </div>
        <div  className=" flex justify-center">
        <MenuNav/>
    </div>
    </div>

    </>
       
    )
}
