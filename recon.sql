-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 29, 2019 at 12:55 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recon`
--

-- --------------------------------------------------------

--
-- Table structure for table `netobjex.com`
--

CREATE TABLE `netobjex.com` (
  `id` int(255) NOT NULL,
  `subdomain` varchar(150) NOT NULL,
  `is_alive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `netobjex.com`
--

INSERT INTO `netobjex.com` (`id`, `subdomain`, `is_alive`) VALUES
(1, 'smartcharge.netobjex.com', 0),
(2, 'netobjex.com', 0),
(3, 'logs.netobjex.com', 1),
(4, 'www.smartcharge.netobjex.com', 1),
(5, 'rockmongo.netobjex.com', 1),
(6, 'coupon.netobjex.com', 0),
(7, 'api2.netobjex.com', 1),
(8, 'xibo.netobjex.com', 1),
(9, 'iotoken-wallet.netobjex.com', 1),
(10, 'survey.netobjex.com', 1),
(11, '104.17.189.74', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tomtom.com`
--

CREATE TABLE `tomtom.com` (
  `id` int(255) NOT NULL,
  `subdomain` varchar(150) NOT NULL,
  `is_alive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tomtom.com`
--

INSERT INTO `tomtom.com` (`id`, `subdomain`, `is_alive`) VALUES
(1, 'c-webfleet.api-system.tomtom.com', 0),
(2, 'fr.support.business.tomtom.com', 1),
(3, 'intranet.tomtom.com', 0),
(4, '1api.tomtom.com', 0),
(5, 'fi.support.tomtom.com', 1),
(6, 'preprod.traffic-stats.tomtom.com', 0),
(7, 'telematics.tomtom.com', 1),
(8, 'backoffice.options.tomtom.com', 0),
(9, '.api2.tomtom.com', 0),
(10, 'qr-api.mapcontent.tomtom.com', 0),
(11, 'www-preview2.business.tomtom.com', 1),
(12, 'api.navcloud.tomtom.com', 0),
(13, 'test-road-event.tomtom.com', 0),
(14, '.business.tomtom.com', 0),
(15, 'no.support.tomtom.com', 1),
(16, 'cs-tst.tomtom.com', 0),
(17, 'api.city.tomtom.com', 0),
(18, 'featurecollectoronline.tomtom.com', 0),
(19, 'it.support.tomtom.com', 1),
(20, 'pantera.mapmaker.tomtom.com', 0),
(21, 'demo-audi-traffic.tomtom.com', 1),
(22, 'changespotting.tomtom.com', 0),
(23, 'pt.support.tomtom.com', 1),
(24, 'sports.beta.tomtom.com', 0),
(25, 'regpnd.services.solaris.test.tomtom.com', 0),
(26, 'gone.tomtom.com', 0),
(27, 'f.cpp-core.tomtom.com', 0),
(28, 'api.trafficviewer.tomtom.com', 0),
(29, 'iphone.tomtom.com', 0),
(30, 'lbsplatform.tomtom.com', 0),
(31, 'mail01.live.telematics.tomtom.com', 0),
(32, '.mcapi-dev.maps.tomtom.com', 0),
(33, 'vpnoffice.business.tomtom.com', 1),
(34, 'maps-imagery.tomtom.com', 0),
(35, 'mtx.tomtom.com', 0),
(36, 'it.support.telematics.tomtom.com', 1),
(37, 'webproxy.algol.test.tomtom.com', 0),
(38, 'home.preprod.tomtom.com', 0),
(39, 'geocoderblog.tomtom.com', 0),
(40, 'dashboard.west-europe.maps-core-prod.tomtom.com', 0),
(41, 'tts.tomtom.com', 0),
(42, 'tts-fca.tomtom.com', 1),
(43, 'test.move.tomtom.com', 0),
(44, 'intershop7.polar.test.tomtom.com', 0),
(45, 'regpnd.services.tomtom.com', 0),
(46, 'a.mysports-preprod.tomtom.com', 1),
(47, 'static.lbs-preprod.tomtom.com', 0),
(48, 'mit-preprod-auth.tomtom.com', 0),
(49, 'stage.api.move.tomtom.com', 0),
(50, 'trafficchallenge.tomtom.com', 0),
(51, 'filetransfer.tomtom.com', 0),
(52, 'rote.tomtom.com', 0),
(53, 'tomtom-uk--tst2.tomtom.com', 1),
(54, 'ns3.telematics.tomtom.com', 1),
(55, 'maps-td-dev.tomtom.com', 0),
(56, 'preprod.tomtom.com', 0),
(57, 'www.live.tomtom.com', 0),
(58, '_sip._tcp.conf.tomtom.com', 0),
(59, 'citymaps.tomtom.com', 0),
(60, 'eu-west-1.maps-pu-poi.tomtom.com', 0),
(61, 'mail302.telematics.tomtom.com', 1),
(62, 'salesforce-sso.tomtom.com', 0),
(63, 'mta4.email.tomtom.com', 0),
(64, 'stub-153.tomtom.com', 1),
(65, 'webproxy.vega.test.tomtom.com', 0),
(66, 'avalon.business.tomtom.com', 1),
(67, 'acheter-gps.tomtom.com', 0),
(68, 'maps.tomtom.com', 1),
(69, 'cpp.tomtom.com', 0),
(70, 'a.routes.tomtom.com', 0),
(71, 'jp.support.tomtom.com', 1),
(72, 'tomtomcrm.tomtom.com', 0),
(73, 'prod.route-monitoring.tomtom.com', 0),
(74, '.production-k8s.mapcontent.tomtom.com', 0),
(75, 'ats.lcms.services.tomtom.com', 1),
(76, 'maps-pu-poi.tomtom.com', 0),
(77, 'fr.support.telematics.tomtom.com', 1),
(78, 'Guest2-eu.tomtom.com', 0),
(79, 'renxinpoce-pushfeeds.tomtom.com', 1),
(80, 'status-001.tomtom.com', 0),
(81, 'webassets.tomtom.com', 1),
(82, 'a.api-internal.tomtom.com', 0),
(83, 'annualreport2013.tomtom.com', 1),
(84, '.ots-app.tomtom.com', 0),
(85, 'www.livetraffic.tomtom.com', 0),
(86, 'reportswithmaps.eu-west-1.maps-central.tomtom.com', 0),
(87, 'preprod.adminarea.od.tomtom.com', 1),
(88, 'home.nebula.test.tomtom.com', 0),
(89, 'connect-nl.tomtom.com', 1),
(90, 'support.tomtom.com', 0),
(91, 'ams-perseus-proxy-audivw-vip.tomtom.com', 0),
(92, 'tachograph.telematics.tomtom.com', 0),
(93, 'partnerlinkdr.tomtom.com', 0),
(94, 'test.navcloud.tomtom.com', 0),
(95, 'us.support.business.tomtom.com', 1),
(96, 'dk.support.telematics.tomtom.com', 1),
(97, 'am3-prod-perseus-audivw-vip.tomtom.com', 0),
(98, 'mgr.conf.tomtom.com', 0),
(99, 'ams2wd-sqlrpt01.tomtom.com', 0),
(100, 'prospect-tts.tomtom.com', 1),
(101, 'move.tomtom.com', 1),
(102, 'babylon.telematics.tomtom.com', 1),
(103, 'ifttt.services.tomtom.com', 0),
(104, 'perseus-storage-002-vip-public.tomtom.com', 0),
(105, 'dev06-ponapi.business.tomtom.com', 1),
(106, 'options.tomtom.com', 0),
(107, 'ats.bms.services.tomtom.com', 1),
(108, 'cert-ams3-traffic.tomtom.com', 1),
(109, 'intershop7.solaris.test.tomtom.com', 0),
(110, 'groups.tomtom.com', 0),
(111, 'prod.tomtom.com', 0),
(112, 'preprod-b.manilla.tomtom.com', 0),
(113, 'eu-west-1.maps-central.tomtom.com', 0),
(114, 'community.solaris.test.tomtom.com', 0),
(115, 'guest1-us.tomtom.com', 0),
(116, 'cdn.tomtom.com', 0),
(117, 'meet.tomtom.com', 0),
(118, 'andrevanduin.tomtom.com', 0),
(119, 'prioritydriving.tomtom.com', 0),
(120, 'oftp.tomtom.com', 0),
(121, 'documentation.maps-transf-dev.tomtom.com', 0),
(122, 'dev-mapshare.tomtom.com', 0),
(123, 'egfia.tomtom.com', 0),
(124, 'b-mydrive.api-system.tomtom.com', 0),
(125, 'www.webfleet.business.tomtom.com', 0),
(126, 'connect-be.tomtom.com', 1),
(127, '0-mail2.tomtom.com', 0),
(128, 'wms03.routes.tomtom.com', 0),
(129, 'qas.tomtom.com', 0),
(130, 'myroute.tomtom.com', 0),
(131, 'streaming.test.navcloud.tomtom.com', 0),
(132, 'webdiams.tomtom.com', 0),
(133, 'places.test.tomtom.com', 0),
(134, 'guest1-ap.tomtom.com', 0),
(135, 'ttggstats.tomtom.com', 0),
(136, 'ahdugahvairo-pushfeeds.tomtom.com', 1),
(137, 'd-webfleet.api-system.tomtom.com', 0),
(138, 'integration-preview.business.tomtom.com', 1),
(139, 'wms03.lbs.tomtom.com', 0),
(140, 'am3-cert-prospect-traffic.tomtom.com', 0),
(141, 'd-mydrive.api-system.tomtom.com', 0),
(142, 'live.telematics.tomtom.com', 0),
(143, 'community.nebula.test.tomtom.com', 0),
(144, 'nl-am3-preprodlb-httpcheck.tomtom.com', 1),
(145, 'fcm-test.tomtom.com', 1),
(146, 'api-internal.navcloud.tomtom.com', 0),
(147, 'proxy-c.city.tomtom.com', 0),
(148, 'www.lifetraffic.tomtom.com', 0),
(149, 'hk-ams.test.tomtom.com', 0),
(150, 'preprod.microservices.city.tomtom.com', 0),
(151, 'pnd.services.solaris.test.tomtom.com', 0),
(152, 'licesning.tomtom.com', 0),
(153, 'dev01-ponapi.business.tomtom.com', 1),
(154, 'sfbaccess.tomtom.com', 0),
(155, 'www.getgoing.tomtom.com', 0),
(156, 'mapshare-beta.tomtom.com', 0),
(157, 'lswebext02.tomtom.com', 0),
(158, 'mta7.email.tomtom.com', 0),
(159, 'discovery.speech.tomtom.com', 0),
(160, 'am2-prod-perseus-saturn-proxy-vip-public.tomtom.com', 0),
(161, 'pre-trafficstats.tomtom.com', 1),
(162, 'preprod-lbs-traffic.tomtom.com', 0),
(163, 'lcms.services.tomtom.com', 1),
(164, 'home.tomtom.com', 0),
(165, 'routes-preprod.tomtom.com', 0),
(166, 'nl.support.telematics.tomtom.com', 1),
(167, 'uk.tomtom.com', 0),
(168, 'a-webfleet.api-system.tomtom.com', 0),
(169, 'prod.traffic-centre.tomtom.com', 0),
(170, 'c.api.internal.tomtom.com', 0),
(171, 'b.api-internal.tomtom.com', 0),
(172, 'archiver.japan.trafficviewer.tomtom.com', 0),
(173, 'mta15.email.tomtom.com', 0),
(174, 'intouch.tomtom.com', 0),
(175, 'api.mydrive.tomtom.com', 0),
(176, 'places.tomtom.com', 0),
(177, 'mapmaker.tomtom.com', 0),
(178, 'audi-cn-traffic.tomtom.com', 1),
(179, 'preprod.samarkandadminconsole.od.tomtom.com', 0),
(180, 'spamfilter.tomtom.com', 0),
(181, 'api-system.tomtom.com', 0),
(182, 'd.raah.tomtom.com', 1),
(183, 'mysports-test.tomtom.com', 0),
(184, 'tts-cna.tomtom.com', 1),
(185, 'geocoder.tomtom.com', 0),
(186, 'bilston-pushfeed-receiver-vip.tomtom.com', 1),
(187, 'test.samarkandadminconsole.od.tomtom.com', 0),
(188, 'midway.tomtom.com', 0),
(189, 'in.support.tomtom.com', 1),
(190, 'es.support.telematics.tomtom.com', 1),
(191, 'tw.tomtom.com', 0),
(192, 'test.archiver.trafficviewer.tomtom.com', 0),
(193, 'annualreport2016.tomtom.com', 0),
(194, '.dcss.asset.tomtom.com', 0),
(195, 'b.cpp-core.tomtom.com', 0),
(196, 'dev09-ponapi.business.tomtom.com', 1),
(197, 'appanalytics.tomtom.com', 0),
(198, 'tw.support.tomtom.com', 1),
(199, 'Guest2-ap.tomtom.com', 0),
(200, '.maps-td.tomtom.com', 0),
(201, 'pushfeeds.tomtom.com', 1),
(202, '3.lbsv2-api.business.tomtom.com', 0),
(203, 'corporate.tomtom.com', 1),
(204, 'prod-perseus-pluto-proxy-vip.tomtom.com', 0),
(205, 'qa-ponapi.telematics.tomtom.com', 1),
(206, 'mta12.email.tomtom.com', 0),
(207, 'connet-au.tomtom.com', 0),
(208, 'dealerstore.tomtom.com', 0),
(209, 'tts-hk2.tomtom.com', 1),
(210, 'mailtest-be.tomtom.com', 0),
(211, 'android.bms.services.tomtom.com', 1),
(212, 'rdw.tomtom.com', 0),
(213, 'lbs-geo.tomtom.com', 0),
(214, 'routes.tomtom.com', 0),
(215, 'home.solaris.test.tomtom.com', 0),
(216, 'community.preprod.tomtom.com', 0),
(217, 'dev.mydrive.tomtom.com', 0),
(218, 'b.dgcache.eu-west-1.maps-imagery.tomtom.com', 0),
(219, 'mta13.email.tomtom.com', 0),
(220, 'agiledays.mapcontent.tomtom.com', 1),
(221, 'www.maps-transf-dev.tomtom.com', 0),
(222, 'preprod-cs-services.api-system.tomtom.com', 0),
(223, 'wms04.lbs.tomtom.com', 0),
(224, 'www.nsk.tomtom.com', 0),
(225, 'api.traffic-centre.tomtom.com', 0),
(226, 'sams-kadmin-001.amsterdam.tomtom.com', 0),
(227, 'dev05-ponapi.business.tomtom.com', 1),
(228, 'api-internal.test.navcloud.tomtom.com', 0),
(229, 'beta.traffic-stats.tomtom.com', 0),
(230, 'prod-perseus-worldwide-neptune-vip.tomtom.com', 0),
(231, 'stage.reine.move.tomtom.com', 0),
(232, 'se.support.tomtom.com', 1),
(233, 'webfleet.tachograph.business.tomtom.com', 0),
(234, 'am3-prod-perseus-mars.tomtom.com', 1),
(235, 'trafficfree.tomtom.com', 0),
(236, 'dawiexiatahf-pushfeeds.tomtom.com', 1),
(237, 'comdeveloper.tomtom.com', 0),
(238, 'mail201.telematics.tomtom.com', 1),
(239, 'cs.tomtom.com', 0),
(240, 'crazywinterweeks.tomtom.com', 0),
(241, 'preprod-bilston-pushfeed-receiver-vip.tomtom.com', 0),
(242, 'test.trafficviewer.tomtom.com', 0),
(243, 'discussions.tomtom.com', 1),
(244, 'sa.services.solaris.test.tomtom.com', 0),
(245, 'engage.tomtom.com', 0),
(246, 'mta16.email.tomtom.com', 0),
(247, 'ap-northeast-2.maps-pu-poi.tomtom.com', 0),
(248, 'Guest1-eu.tomtom.com', 0),
(249, '.telematics.tomtom.com', 0),
(250, 'laoluojiayou-pushfeeds.tomtom.com', 0),
(251, 'sipexternal.tomtom.com', 0),
(252, 'image.email.tomtom.com', 1),
(253, 'api2.tomtom.com', 0),
(254, 'appanalytics-dev.tomtom.com', 0),
(255, 'gslb.tomtom.com', 0),
(256, 'test.internal.api.od.tomtom.com', 0),
(257, 'www.routes.tomtom.com', 0),
(258, 'ttconfigcmg.tomtom.com', 0),
(259, 'webfleet3.telematics.tomtom.com', 1),
(260, 'hyundai-kia-ams.services.tomtom.com', 0),
(261, 'hub.discussions.tomtom.com', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `netobjex.com`
--
ALTER TABLE `netobjex.com`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `subdomain` (`subdomain`);

--
-- Indexes for table `tomtom.com`
--
ALTER TABLE `tomtom.com`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `subdomain` (`subdomain`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `netobjex.com`
--
ALTER TABLE `netobjex.com`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `tomtom.com`
--
ALTER TABLE `tomtom.com`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=262;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
