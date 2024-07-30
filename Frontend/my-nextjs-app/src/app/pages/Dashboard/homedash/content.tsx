import React from "react";
import Head from "next/head";

export default function CatalogDashboard(){
    return(
        <>
        <Head>
        <title>Recomendation Product</title>
        </Head>
        <div className="grid grid-cols-3 gap p-6 ">
            {/* <img src="" alt=""></img> */}
            <p>product 1</p>
            <p>product 2</p>
            <p>product 3</p>
        </div>
       
        </>

    )
}