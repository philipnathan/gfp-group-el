import Image from "next/image";
import NavbarPage from "./pages/Dashboard/navbar"
import HomeDashboard from "./pages/Dashboard/homedash";
import FooterDash from "./pages/Dashboard/footer";
import ArticleDash from "./pages/Dashboard/article";
import Head from "next/head";


export default function Home() {
  return (
    <div>
      <Head>
        <title>PDC RYCYCLE</title>
      <link 
            rel='stylesheet'
            href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css'
            />
      </Head>
      <NavbarPage/>
      <div className="pt-20">
      <HomeDashboard/>
      <ArticleDash/>
      <FooterDash/>
      </div>
    </div>
  );
}
