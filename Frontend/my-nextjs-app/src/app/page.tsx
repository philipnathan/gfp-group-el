import Image from "next/image";
import NavbarPage from "./component/navbar";
import FooterDash from "./component/footer";
import ArticleDash from "./component/article";
import HomePage from "./component/homedash";
import Head from "next/head";


export default function MainPage() {
  return (
    <div>
      <Head>
        <title>PDC RYCYCLE</title>
        <link
          rel="stylesheet"
          href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
        />
      </Head>
      <NavbarPage />
      <div className="pt-20">
        <HomePage />
        <ArticleDash />
        <FooterDash />
      </div>
    </div>
  );
}
