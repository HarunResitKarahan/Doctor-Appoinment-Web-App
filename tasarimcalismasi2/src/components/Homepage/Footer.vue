<template>
  <div class="site-footer">
    <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>About</h6>
            <p class="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Bölümler</h6>
            <ul class="footer-links">
              <li><a href="#">Dahiliye<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Kulak Burun Boğaz<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Cildiye<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Fizik Tedavi<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Ortopedi<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Kardiyoloji<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Kalp Damar Cerrahi<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Çocuk Cerrahi<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
            </ul>
          </div>

          <div class="col-xs-6 col-md-3">
            <ul class="footer-links" style="margin-top: 31.19px">
              <li><a href="#">Göz Hastalıkları<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Nöroloji<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Psikiyatri<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Göğüs Hastalıkları<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Göğüs Cerrahi<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Çocuk Hastalıkları<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
              <li><a href="#">Kadın Doğum<div class="underline" style="background: white; margin-top: 3px;"></div></a></li>
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-8 col-sm-6 col-xs-12">
            <p class="copyright-text">Copyright &copy; 2021
         Harun Reşit KARAHAN.
            </p>
          </div>

          <div class="col-md-4 col-sm-6 col-xs-12">
            <ul class="social-icons">
              <li><a class="facebook" href="#"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-facebook"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a></li>
              <li><a class="twitter" href="#">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-twitter"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a></li>
              <li><a class="linkedin" href="#">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a></li>
            </ul>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Footer',
  mounted () {
    $(document).ready(function () {
      $('.footer-links li a').mouseenter(function () {
        $(this).find('.underline').animate({ width: '100%', left: '0' }, 100, function () {
          $('.footer-links li a').mouseleave(function () { $(this).find('.underline').animate({ width: '0', left: '50%' }, 0) })
        })
      })
    })
  }
}
</script>
