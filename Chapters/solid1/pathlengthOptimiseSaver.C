void pathlengthOptimiseSaver() {
	TFile * fIn1 = new TFile("~/workspace/saffron/Saffron-histos_simWeighted.root");
  TFile * fIn2 = new TFile("~/workspace/saffron/Saffron-histos_simNonWeighted.root");

  TH1F * h1 = fIn2->Get("SafSimComparison/pathlengthResidual");
  TH1F * h2 = fIn1->Get("SafSimComparison/pathlengthResidual");
  TH1F * h3 = fIn1->Get("SafSimComparison/pathlengthResidual_cuts");

  h2->SetName("pathlengthResidual_weighted");
  h2->SetTitle("pathlengthResidual_weighted");

  h3->SetName("thinned");
  h3->SetTitle("thinned");

  TFile * fOut = new TFile("pathlengthOptimisePlots.root", "RECREATE");
  h1->Write();
  h2->Write();
  h3->Write();
}