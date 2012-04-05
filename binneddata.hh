#ifndef __BINNED_DATA_HH__
#define __BINNED_DATA_HH__

#include "fit.hh"


class TH1D;

TH1D* getData(const std::vector<std::string>& filenames, const char* histname, int nbins, double* bins);

#endif
