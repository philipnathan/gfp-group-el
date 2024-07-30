import Head from "next/head";
import "../../../globals.css";
import SosialMedia from "./sosialmedia";


export default function FooterDash(){
    return(
        <>
        <Head>
          <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
          />
          </Head>
          <div className="bg-white">
          <SosialMedia/>
          <div className="bg-white min-h-screen flex items-center justify-center">
          <p>Layanan Pelanggan</p>
          <br/>
          <p>bantuan</p>
          <br/>
          <p>Metode Pembayaran</p>
          </div>
          </div>
        
   
      </>
    )
}