import Image from "next/image";
import NavbarPage from "./pages/Dashboard/navbar"
import HomeDashboard from "./pages/Dashboard/homedash";
import FooterDash from "./pages/Dashboard/footer";
import ArticleDash from "./pages/Dashboard/article";


export default function Home() {
  return (
    <div>
      <NavbarPage/>
      <div className="pt-20">
      <HomeDashboard/>
      <ArticleDash/>
      <FooterDash/>
      </div>
    
    
    </div>
  );
}
